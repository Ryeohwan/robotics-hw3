#!/usr/bin/env python
import rospy
from topic_custom.msg import TimePose

def callback(msg):
    print "subscribe:", msg.timestamp.secs%100, msg.pose.x, msg.pose.y, msg.pose.theta

rospy.init_node('algorithm_subscriber')
sub = rospy.Subscriber('common_msg', TimePose, callback)
rospy.spin()
