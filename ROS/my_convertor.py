#!/usr/bin/env python
 

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
import numpy as np
from math import atan2,asin
from std_msgs.msg import String
from beginner_tutorials.msg import quaternion
from beginner_tutorials.msg import euler

msgs=quaternion()
def callback(msg):
    
    msgs= msg
    q0=msgs.quaternionX
    q1=msgs.quaternionY
    q2=msgs.quaternionZ
    q3=msgs.quaternionW
    roll1 = (180/3.14)*atan2(2*(q0*q1+q2*q3),1-2*(q1*q1+q2*q2))
    pitch1= 0#(180/3.14)*asin(2*(q0*q2-q3*q1))
    yaw1=(180/3.14)*atan2(2*(q0*q3+q1*q2),1-2*(q3*q3+q2*q2))
    pub = rospy.Publisher('chatter', euler, queue_size=10)
    eu=euler()
    eu.roll=roll1
    eu.pitch=pitch1
    eu.yaw=yaw1
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():

        pub.publish(eu)
        rate.sleep()
    print(msg)

def listener():
    global msgs
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('my_convertor', anonymous=True)

    rospy.Subscriber('quaternion', quaternion, callback)
   # q0=msgs.quaternionX
   # q1=msgs.quaternionY
    #q2=msgs.quaternionZ
    #q3=msgs.quaternionW
    #roll1 = (180/3.14)*math.atan2(2*(q0*q1+q2*q3),1-2*(q1*q1+q2*q2))
    #pitch1= (180/3.14)*math.asin(2*(q0*q2-q3*q1))
    #yaw1=(180/3.14)*math.atan2(2*(q0*q3+q1*q2),1-2*(q3*q3+q2*q2))
    #pub = rospy.Publisher('chatter', euler, queue_size=10)
    #eu=euler()
    #eu.roll=roll1
    #eu.pitch=pitch1
    #eu.yaw=yaw1
    #rate = rospy.Rate(10) # 10hz
    #while not rospy.is_shutdown():

       # pub.publish(eu)
       # rate.sleep()
         
    #quat=quaternion()
    #quat.quaternionX

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
