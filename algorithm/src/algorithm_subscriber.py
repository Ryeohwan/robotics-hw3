#!/usr/bin/env python
import rospy
from common_msgs.msg import TimePose
from common_msgs.srv import hw3, hw3Response

def callback(msg):
    print "subscribe:", msg.info, msg.pose.x, msg.pose.y, msg.pose.theta
def service_callback(request):
    response = hw3Response(sum=request.a + request.b)
    print "satisfied condition", request.a, request.b, "find a mineral amount:", response.sum
    return response
rospy.init_node('algorithm_subscriber')
sub = rospy.Subscriber('common_msgs', TimePose, callback)
service = rospy.Service('hw3', hw3, service_callback)
rospy.spin()
