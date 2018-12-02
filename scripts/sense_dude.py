#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image

def update_depth(data):
    print 'yeet'
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def sense_symbol(data):
    print 'oof'
    
def listener():
        
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('sense_dude', anonymous=True)

    depth_maybe = "camera/aligned_depth_to_color/image_raw"
    color_maybe = "camera/color/image_raw"
    
    rospy.Subscriber(depth_maybe, Image, update_depth)
    rospy.Subscriber(color_maybe, Image, sense_symbol)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    
if __name__ == '__main__':
    listener()