#! /usr/bin/env python
# -*- coding: utf-8 -*-

import roslib
roslib.load_manifest('learning_tf')
import rospy

import tf
from tf.transformations import quaternion_from_euler
import turtlesim.msg

def handle_turtle_pose(msg, turtlename):
    br = tf.TransformBroadcaster()
    
    # 2个坐标系位置关系
    br.sendTransform((msg.x, msg.y, 0),
                     quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     'world')


if __name__=="__main__":
    rospy.init_node('turtle_tf_broadcaster')
    turtlename = rospy.get_param('~turtle') 
    rospy.Subscriber('/%s/pose' % turtlename,
                     turtlesim.msg.Pose,
                     handle_turtle_pose,
                     turtlename)
    rospy.spin()