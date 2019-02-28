# robG13
A repository for the collaboration of group 13 in completing workshop tasks for the Autonomous Mobile Robotics module of the University of Lincoln's Computer Science BSc course.

# Discord Link
https://discordapp.com/invite/dk8Eht

# Authors
* [Laurence Elliott](https://github.com/laurencejbelliott)
* [Kostadin Yankov](https://github.com/KostadinYankov)
* [Sam Chambers](https://github.com/UoLSChambers)
* [Elliot Kemp](https://github.com/ElliotK134)

# Running in simulation
1. Install the prerequesite packages from LCAS in Ubuntu 16.04 by following the steps at [https://github.com/LCAS/rosdistro/wiki#using-the-l-cas-repository-if-you-just-want-to-use-our-software](https://github.com/LCAS/rosdistro/wiki#using-the-l-cas-repository-if-you-just-want-to-use-our-software).
2. Run `sudo apt-get update && sudo apt-get upgrade && sudo apt-get install ros-kinetic-uol-cmp3103m` to ensure that packages are up-to-date, and that the correct course specific packages are installed.
3. Create a catkin workspace with the following commands:
* `mkdir -p ~/workspace/src`
* `cd ~/workspace/src`
* `catkin_init_workspace`
* `cd ..`
* `catkin_make`
4. Setup environment variables for your terminal (do this for each new terminal that you want to use to interact with the robot simulation) with `source ~/workspace/devel/setup.bash`
5. Launch the simulation of the turtlebot, including `roscore` and `gazebo` with the command `roslaunch turtlebot_gazebo turtlebot_world.launch world_file:=$(rospack find turtlebot_gazebo)/worlds/empty.world`.
6. To interact with the simulation via `rviz`, run `roslaunch turtlebot_rviz_launchers view_robot.launch`.
7. Open a new terminal and repeat step 4 before running any Python scripts, either directly with `python <name of python file>`, or via an IDE such as Spyder e.g. `spyder <name of python file>`.

# Running on the robot
1. Download `ros-network.sh` and `rpi.ovpn` from this repository.  These files have been edited to match the ip address of our robot.  The rpi.ovpn file was previously available from the web server hosted on the raspberry pi, but required modification to match the ip address of the robot.
2. Connect to the web server hosted on the raspberry pi in browser.  The ip address is http://10.82.0.103/.  From here, go into the tmule control and start the turtlebot and roscore services.  If the later steps don't work, click the check button to ensure that they're running properly.
3. Run the vpn client: `sudo openvpn <filepath>/rpi.ovpn`.  This vpn must be kept running.  The pc is now connected to the robot via a vpn.  The robot has the address 192.168.2.1.
4. For ros commands to be run on the robot, not the local pc, a few environment variables have to be set so ros knows where to run these commands.  This is the purpose of ros-network.sh.  It's a bash script that will set these environment variables up.  In each terminal that we want to use to run commands on the robot, we need to source those environment variables using the script: `source ~/ros-network.sh 192.168.2.1`.  
5. You can verify that this has worked successfully by running `rostopic list`.  `roslaunch turtlebot_rviz_launchers view_robot.launch` will launch rviz, which should show us the view from the kinect on the robot.
6. Starting spyder in this terminal should actually cause any code run through spyder to work on the robot.

# Assignment Environment:
- `sudo apt update`
- `sudo apt upgrade`

1. Open environment with the map and poles:
* `roslaunch uol_turtlebot_simulator object-search-training.launch` 

2. Open the correct Rviz for this environment:
* `roslaunch turtlebot_rviz_launchers view_robot.launch`

3. Keyop if must:
* `roslaunch kobuki_keyop keyop.launch` 



