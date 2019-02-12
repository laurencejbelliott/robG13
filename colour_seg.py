#!/usr/bin/env python

import rospy
import cv2
import numpy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class image_converter:

    def __init__(self):

        cv2.startWindowThread()
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",
                                          Image, self.callback)
        self.string_pub = rospy.Publisher("/result_topic", String, queue_size=1)

    def callback(self, data):
        cv2.namedWindow("Image window", 1)
        cv2.namedWindow("Thresholded image window", 2)
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError, e:
            print e

        bgr_thresh = cv2.inRange(cv_image,
                                 numpy.array((60, 0, 25)),
                                 numpy.array((75, 120, 255)))

        hsv_img = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        hsv_thresh = cv2.inRange(hsv_img,
                                 numpy.array((0, 90, 0)),
                                 numpy.array((360, 100, 250)))

        _, bgr_contours, hierachy = cv2.findContours(
            bgr_thresh.copy(),
            cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE)
        for c in bgr_contours:
            a = cv2.contourArea(c)
            if a > 0.001:
                cv2.drawContours(cv_image, c, -1, (0, 255, 0))

        _, hsv_contours, hierachy = cv2.findContours(
            hsv_thresh.copy(),
            cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE)
        for c in hsv_contours:
            a = cv2.contourArea(c)
            if a > 100.0:
                cv2.drawContours(cv_image, c, -1, (255, 0, 0))
        cv2.imshow("Image window", cv_image)

        threshImg = cv2.bitwise_and(cv_image, cv_image, mask=bgr_thresh)
        cv2.imshow("Thresholded image window", threshImg)
        self.string_pub.publish(str(numpy.mean(threshImg[:,:,2])))

        cv2.waitKey(1)


image_converter()
rospy.init_node('image_converter', anonymous=True)
rospy.spin()
cv2.destroyAllWindows()