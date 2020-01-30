# **Requirements**

* Python
* Ros
* Gazebo
* OpenCv









# **Steps for to do before run the simulation:**

This project was make in Ros Melodic.

* Install the simulator Husky robot of clearpath (attencion for your Ros 
version) this will be installed on Ros folder:

`$ 'sudo apt-get install ros-melodic-husky-simulator` 

* And install the Husky desktop:  `$ 'sudo apt-get install ros-indigo-husky-desktop'`

* Clone this repository to your workspace inside src folder: 

* [Velodyne VLP-16](https://bitbucket.org/DataspeedInc/velodyne_simulator.git)

* [Senai Cimatec 4 Map](https://github.com/Brazilian-Institute-of-Robotics/bir.cimatec4_map.git)

* [Point Cloud to Laser Scan](https://github.com/ros-perception/pointcloud_to_laserscan.git)

* [Frontier Exploration](https://github.com/paulbovbel/frontier_exploration.git)

* [Navigation 2D](https://github.com/skasperski/navigation_2d.git)

Make this changes:

-- Go to folder navigation_2d --> nav2d_karto --> OpenKarto --> source --> OpenKarto --> Sensor.h
In line 430 delete +1 and save











