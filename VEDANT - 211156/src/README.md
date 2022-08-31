1 .added sensors ,camera and imu to the robot by updating m2wr.gazebo, rviz.launch and m2wr.xacro file.

2.  robotmodel.rviz file is created.

3. gmapping node is added to the file rviz.launch.

Launching code: 

1. source ~/simulation_ws/devel/setup.bash

2. roslaunch demo-gazebo my_world.launch .
 
3. roslaunch m2wr_description spawn.launch 

4. roslaunch m2wr_description rviz.launch

4. rostopic pub /cmd_vel geometry_msgs/Twist -- '[0.0,0.0,0.0]' '[1.0,0.0,1.0]'


youtube link :- https://www.youtube.com/watch?v=yrqR7Pp09ZQ
