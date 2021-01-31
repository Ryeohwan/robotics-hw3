#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose2D
from common_msgs.msg import TimePose
from common_msgs.srv import hw3, hw3Request

rospy.init_node('sensor_publisher')
rospy.wait_for_service('hw3')
requester = rospy.ServiceProxy('hw3', hw3)
pub = rospy.Publisher('common_msgs', TimePose, queue_size=1)
msg = TimePose()
rate = rospy.Rate(1)
msg.info.data = 0

while not rospy.is_shutdown():
    msg.info.data += 11
    msg.pose = Pose2D(x=msg.info.data%9*7, y=msg.info.data%7*9, theta=msg.info.data%5*9)
    if msg.pose.x < 40:
        req = hw3Request(a=msg.pose.x, b=msg.pose.y)
        res = requester(req)
        print "satisfied condition", req.a, req.b, "find a mineral amount:", res.sum
    pub.publish(msg)
    print "publish:", msg.info, msg.pose.x, msg.pose.y, msg.pose.theta
    rate.sleep()
    
