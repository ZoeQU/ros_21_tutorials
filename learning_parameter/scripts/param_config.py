#! /usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import rospy
from std_srvs.srv import Empty

def parameter_config():
    # 初始化节点
    rospy.init_node('parameter_config', anonymous=True)

    # 得到当前参数（背景颜色）
    red = rospy.get_param('turtlesim/background_r')
    blue = rospy.get_param('turtlesim/background_b')
    green = rospy.get_param('turtlesim/background_g')

    rospy.loginfo('get background color [%d, %d, %d]', red, green, blue)

    # 设置新参数（背景颜色）
    rospy.set_param('turtlesim/background_b', 255)
    rospy.set_param('turtlesim/background_g', 255)
    rospy.set_param('turtlesim/background_r', 255)

    # 打印设置后的结果
    rospy.loginfo('set background color [255,255,255]')

    # 得到新参数（背景颜色）
    red = rospy.get_param('turtlesim/background_r')
    blue = rospy.get_param('turtlesim/background_b')
    green = rospy.get_param('turtlesim/background_g')

    rospy.loginfo('get background color [%d, %d, %d]', red, green, blue)

    # 发现'/clear'服务并链接
    rospy.wait_for_service('/clear')

    try:
        clear_background = rospy.ServiceProxy('/clear', Empty)
        response = clear_background()
        return response
    
    except rospy.ServiceException as e:
        print('service call failed: %s' % e)

if __name__ == "__main__":
    parameter_config()