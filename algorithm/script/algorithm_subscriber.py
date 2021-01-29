#!/usr/bin/env python
import rospy
from common_msgs.msg import TimePose


def callback(msg):
    print "subscribe:", msg.info, msg.pose.x, msg.pose.y, msg.pose.theta

rospy.init_node('algorithm_subscriber')
sub = rospy.Subscriber('common_msgs', TimePose, callback)
rospy.spin()
