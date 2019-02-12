#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def set_velocity():
    pub = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size=10)
    rospy.init_node('set_velocity', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        twist_msg = Twist()
        twist_msg.linear.x = 0.0
        twist_msg.linear.y = 0.0
        twist_msg.linear.z = 2
        twist_msg.angular.x = 0.0
        twist_msg.angular.y = 0.0
        twist_msg.angular.z = 2
        rospy.loginfo(twist_msg)
        pub.publish(twist_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        set_velocity()
    except rospy.ROSInterruptException:
        pass