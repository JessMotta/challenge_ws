#!/usr/bin/env python2.7

#Import libraries:
import rospy
from sensor_msgs.msg import Image
import cv2
import time
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Int32
from sensor_msgs.msg import Image

#Define Class:
class Camera:
  
  def __init__(self):
    rospy.init_node('opencv_camera', anonymous=True)
    self.pub = rospy.Publisher("camera/detect_ball", Image, queue_size=10)
    self.bridge = CvBridge()
    rospy.loginfo("Camera was initialized")
    self.start = time.time()
    #range definition:
    self.yellow_range = [(25, 50, 50), (32, 255, 255)]
    

  def color_circle_detector(self, cv_image):
    # timer count and font:
    timer = int(time.time() - self.start)
    font = cv2.FONT_HERSHEY_SIMPLEX

    #convert img to cv2:
    cv2_frame = self.bridge.imgmsg_to_cv2(cv_image, "bgr8")
    
    #hsv convert and create a mask:
    hsv = cv2.cvtColor(cv2_frame, cv2.COLOR_BGR2HSV)
    mask_yellow = cv2.inRange(hsv, self.yellow_range[0], self.yellow_range[1])
    mask_yellow = cv2.erode(mask_yellow, None, iterations=2)
    mask_yellow = cv2.dilate(mask_yellow, None, iterations=2)
    cnt_yellow = cv2.findContours(mask_yellow.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    #detect circle:
    contours_poly = []
    centers = []
    radius = []
    for index, obj_cnt in enumerate(cnt_yellow):
      contours_poly.append(cv2.approxPolyDP(obj_cnt, 0.009 * cv2.arcLength(obj_cnt, True), True))
      aux1, aux2 = cv2.minEnclosingCircle(contours_poly[index])
      centers.append(aux1)
      radius.append(aux2)
      if(len(contours_poly[index]) > 10):
        #identify the sphere and send a message the was detect the sphere:
        cv2.circle(cv2_frame, (int(centers[index][0]), int(centers[index][1])), int(radius[index]), (150, 20, 255), 6)
        cv2.putText(cv2_frame, 'TARGET WAS DETECTED!!', (400,150), font, 2, (50, 50, 255), 5)

    #merge the info about time into frame:
    cv2.putText(cv2_frame, str(timer) + 's', (20, 60), font, 2, (226, 43, 138), 5)
    cv2.putText(cv2_frame, str(time.ctime()), (10, 700), font, 2, (226, 43, 138), 6)

    #convert the image to ros and publish the image:
    ros_frame = self.bridge.cv2_to_imgmsg(cv2_frame, "bgr8")
    self.pub.publish(ros_frame)

  def listener(self):
    #subscribe:
    rospy.Subscriber('/diff/camera_top/image_raw', Image, self.color_circle_detector)

    #keeping python until node stopped:
    rospy.spin()

#main function:
if __name__ == "__main__":
  try:
    cam_print = Camera()
    cam_print.listener()
  except rospy.ROSInterruptException:
    pass