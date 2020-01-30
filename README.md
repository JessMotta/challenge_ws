# **Project** :robot: :wolf: :dart: :octocat:

This project was make to autonomous navigation for Husky Clearpath simulated in Gazebo to found an yellow ball.



# **Requirements**
This requirements are the minimal to execute this package:

* Python 2.7
* Ros Melodic
* Gazebo 9
* OpenCv 3.2









# **Steps for to do before run the simulation:**

This project was make in Ros Melodic.

* Install the simulator Husky robot of clearpath (attencion for your Ros 
version) this will be installed on Ros folder:

`$ sudo apt-get install ros-melodic-husky-simulator` 

* And install the Husky desktop:  `$ sudo apt-get install ros-indigo-husky-desktop'`

* Clone this repository to your workspace inside src folder: 

* [Velodyne VLP-16](https://bitbucket.org/DataspeedInc/velodyne_simulator.git)

* [Senai Cimatec 4 Map](https://github.com/Brazilian-Institute-of-Robotics/bir.cimatec4_map.git)

* [Point Cloud to Laser Scan](https://github.com/ros-perception/pointcloud_to_laserscan.git)

* [Frontier Exploration](https://github.com/paulbovbel/frontier_exploration.git)

* [Navigation 2D](https://github.com/skasperski/navigation_2d.git)

![cimatec_gazebo](https://user-images.githubusercontent.com/30941796/73447951-95e3f780-433e-11ea-8082-63e399cf9e94.png)
Attencion: This map was made by Azihel, Pedro Paulo and Jean Paulo.

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


# **Order to Execute the Launchs:**

* `$ roslaunch gazebo_senai gazebo.launch`

* `$ roslaunch gazebo_senai rviz.launch`

* `$ roslaunch gazebo_senai exploration.launch`














