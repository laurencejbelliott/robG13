
wheel_radius = .1
robot_radius = 1

# computing the forward kinematics for a differential drive
def forward_kinematics(w_l, w_r):
    c_l = wheel_radius * w_l
    c_r = wheel_radius * w_r
    v = (c_l + c_r) / 2
    a = (c_r - c_l) / (2 * robot_radius)
    return (v, a)


# computing the inverse kinematics for a differential drive
def inverse_kinematics(v, a):
    c_l = v - (robot_radius * a)
    c_r = v + (robot_radius * a)
    w_l = c_l / wheel_radius
    w_r = c_r / wheel_radius
    return (w_l, w_r)


# inverse kinematics from a Twist message (This is what a ROS robot has to do)
def inverse_kinematics_from_twist(t):
    return inverse_kinematics(t.linear.x, t.angular.z)
    

def wlVelCB(data):
    print(data)
    v, a = forward_kinematics(float(data.data), 0.0)
    print(v, a)
    
    tw = Twist()
    tw.linear.x = v
    tw.angular.z = a
    print(tw)
    rTwistPub.publish(tw)


if __name__ == "__main__":
    import rospy
    from std_msgs.msg import Float32
    from geometry_msgs.msg import Twist
    
    rospy.init_node(name="kinematics_ws")
    wheel_vel_left_pub =  rospy.Publisher("/wheel_vel_left", Float32, 
                                          queue_size=1)
    
    rTwistPub = rospy.Publisher("/cmd_vel_mux/input/navi", Twist, queue_size=1)
    wl_vel_sub = rospy.Subscriber("/wheel_vel_left", Float32, 
                                  callback=wlVelCB)
    
    
#==============================================================================
#     (w_l, w_r) = inverse_kinematics(0.0, 1.0)
#     print "w_l = %f,\tw_r = %f" % (w_l, w_r)
# 
#     (v, a) = forward_kinematics(w_l, w_r)
#     print "v = %f,\ta = %f" % (v, a)
# 
#     from geometry_msgs.msg import Twist
#     t = Twist()
# 
#     t.linear.x = 0.3
#     t.angular.z = 0.8
# 
#     (w_l, w_r) = inverse_kinematics_from_twist(t)
#     print "w_l = %f,\tw_r = %f" % (w_l, w_r)
#==============================================================================
    
    rospy.spin()
