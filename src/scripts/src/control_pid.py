import rospy

class ControlPid:
  sat_max = 0
  sat_min = 0
  kp = 0
  ki = 0
  kd = 0
  error_integral = 0 
  error_prev = 0 

  def __init__ (self, sat_max, sat_min, kp, ki, kd):
    rospy.init_node("robot_vision", anonymous=True)
    self.sat_max = sat_max 
    self.sat_min = sat_min 
    self.kp = kp 
    self.ki = ki 
    self.kd = kd 
    
  def pid_calculate(self, time, setpoint, process):
    self.error = setpoint - process
    self.error_integral =+ self.error
    control_input = self.kp*self.error + self.ki*(self.error_integral)*time + self.kd*(self.error - self.error_prev)/time
    
    if (control_input > self.sat_max):
      control_input = self.sat_max
    elif (control_input < self.sat_min):
      control_input = self.sat_min
   
    self.error_prev = self.error
    return control_input