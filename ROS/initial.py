#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def initial():
    rospy.init_node('initialize', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    all_msgs=[]
    msg=Twist()
    msg.linear.x=0
    msg.linear.y=0
    msg.linear.z=0
    msg.angular.x=0
    msg.angular.y=0
    msg.angular.z=1
    all_msgs.append(msg)
    msg=Twist()
    msg.linear.x=1
    msg.linear.y=0
    msg.linear.z=0
    msg.angular.x=0
    msg.angular.y=0
    msg.angular.z=0
    all_msgs.append(msg)
    msg=Twist()
    msg.linear.x=0
    msg.linear.y=0
    msg.linear.z=0
    msg.angular.x=0
    msg.angular.y=0
    msg.angular.z=-2
    all_msgs.append(msg)
    msg=Twist()
    msg.linear.x=2
    msg.linear.y=0
    msg.linear.z=0
    msg.angular.x=0
    msg.angular.y=0
    msg.angular.z=0
    all_msgs.append(msg)
    msg=Twist()
    msg.linear.x=-1
    msg.linear.y=0
    msg.linear.z=0
    msg.angular.x=0
    msg.angular.y=0
    msg.angular.z=0
    all_msgs.append(msg)
    msg=Twist()
    msg.linear.x=0
    msg.linear.y=0
    msg.linear.z=0
    msg.angular.x=0
    msg.angular.y=0
    msg.angular.z=-2
    all_msgs.append(msg)
    msg=Twist()
    msg.linear.x=1
    msg.linear.y=0
    msg.linear.z=0
    msg.angular.x=0
    msg.angular.y=0
    msg.angular.z=0
    all_msgs.append(msg)
    msg=Twist()
    msg.linear.x=0
    msg.linear.y=0
    msg.linear.z=0
    msg.angular.x=0
    msg.angular.y=0
    msg.angular.z=1
    all_msgs.append(msg)
    msg=Twist()
    msg.linear.x=1
    msg.linear.y=0
    msg.linear.z=0
    msg.angular.x=0
    msg.angular.y=0
    msg.angular.z=0
    all_msgs.append(msg)
    msg=Twist()
    msg.linear.x=1
    msg.linear.y=0
    msg.linear.z=0
    msg.angular.x=0
    msg.angular.y=0
    msg.angular.z=0
    all_msgs.append(msg)

    rate = rospy.Rate(1)
    i=len(all_msgs)
    n=0
    while not rospy.is_shutdown():
            if n==i:
                break
        
            pub.publish(all_msgs[n])
            n=n+1
            rate.sleep()
             
    
if __name__ == '__main__':
    try:
        initial()
    except rospy.ROSInterruptException:
        pass
  
