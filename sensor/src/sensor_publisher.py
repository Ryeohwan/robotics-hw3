#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose2D
from common_msgs.msg import TimePose


rospy.init_node('sensor_publisher')
pub = rospy.Publisher('common_msgs', TimePose, queue_size=1)
msg = TimePose()
rate = rospy.Rate(1)
msg.info.data = 0

while not rospy.is_shutdown():
    msg.info.data += 9
    msg.pose = Pose2D(x=msg.info.data%4, y=msg.info.data%7, theta=msg.info.data%5)
    pub.publish(msg)
    print "publish:", msg.info, msg.pose.x, msg.pose.y, msg.pose.theta
    rate.sleep()
