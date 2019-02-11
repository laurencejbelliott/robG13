# robG13
A repository for the collaboration of group 13 in completing workshop tasks for the Autonomous Mobile Robotics module of the University of Lincoln's Computer Science BSc course.

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
* `cd ~/workspace`
* `catkin create`
4. Setup environment variables for your terminal (do this for each new terminal that you want to use to interact with the robot simulation) with `source ~/workspace/devel/setup.bash`
5. Launch the simulation of the turtlebot, including `roscore` and `gazebo` with the command `roslaunch turtlebot_gazebo turtlebot_world.launch world_file:=$(rospack find turtlebot_gazebo)/worlds/empty.world`.
6. Open a new terminal and repeat step 4 before running any Python scripts, either directly with `python <name of python file>`, or via an IDE such as Spyder e.g. `spyder <name of python file>`.
