#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def set_velocity():
    # sets up a publisher, publishing message type Twist to arg1.
    pub = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size=10)
    # initialises the node which will communicate with rospy
    # so the node 'set_velocity' is now publishing to mobile_base/commands/velocity
    rospy.init_node('set_velocity', anonymous=True)
    # this object is a quick way of calling a function x times a second
    # sleep() will sleep for just long enough to maintain the frequency per second
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        twist_msg = Twist()
        twist_msg.linear.x = 0.0
        twist_msg.linear.y = 0.0
        twist_msg.linear.z = 2
        twist_msg.angular.x = 0.0
        twist_msg.angular.y = 0.0
        twist_msg.angular.z = 2
        rospy.loginfo(twist_msg) # logs to terminal screen, but also to rosout and node log file
        pub.publish(twist_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        set_velocity()
    except rospy.ROSInterruptException:
        pass