#!/usr/bin/env python

import numpy

import cv2
import cv_bridge
import rospy

from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist


class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        self.image_sub = rospy.Subscriber('/camera/rgb/image_raw', Image,
                                          self.image_callback)
        self.depth_image_sub = rospy.Subscriber('/camera/depth_registered/image_raw', Image,
                                          self.depth_image_callback)
        self.cmd_vel_pub = rospy.Publisher('/mobile_base/commands/velocity', Twist,
                                           queue_size=1)
        self.depth_image_CV2 = None
        self.twist = Twist()


    def depth_image_callback(self, data):
        self.depth_image_CV2 = self.bridge.imgmsg_to_cv2(data, "32FC1")


    def image_callback(self, msg):
        cv2.namedWindow("window", 1)
        cv2.namedWindow("colourSeg", 2)
        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_red = numpy.array([0, 120, 100])
        upper_red = numpy.array([20, 360, 360])
        mask = cv2.inRange(hsv, lower_red, upper_red)
        colourSegImage = cv2.bitwise_and(image, image, mask=mask)
        colourSegImage = cv2.medianBlur(colourSegImage, 1)
        h, w, d = image.shape
        search_top = h / 4
        search_bot = 3*h/4 + 20
        mask[0:search_top, 0:w] = 0
        mask[search_bot:h, 0:w] = 0
        M = cv2.moments(mask)
        if M['m00'] > 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            # cv2.circle(image, (cx, cy), 20, (255, 0, 255), -1)
            cv2.circle(image, (cx, cy), 20, (255, 0, 255), -1)
            err = cx - w/2
            self.twist.linear.x = 0.2
            self.twist.angular.z = -float(err) / 200

            cDepth = self.depth_image_CV2[cy, cx]
            print(cDepth)

            if cDepth < 1000:
                self.twist.linear.x = 0.0
                self.twist.angular.z = 0.0


            self.cmd_vel_pub.publish(self.twist)
        cv2.imshow("window", image)
        cv2.imshow("colourSeg", colourSegImage)
        cv2.waitKey(3)


cv2.startWindowThread()
rospy.init_node('follower')
follower = Follower()
rospy.spin()

cv2.destroyAllWindows()


