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


![](/home/jess/challenge_ws/src/bir.cimatec4_map/doc/cimatec_gazebo.png)

Make this changes:

* Go to:
<ol>
  <li>folder navigation_2d </li> 
  <li>nav2d_karto </li> 
  <li>OpenKarto,/li> 
  <li>source </li> 
  <li>OpenKarto</li> 
  <li> Open in Vscode or any other: Sensor.h: change the line 430 delete +1 and save </li>
</ol>











