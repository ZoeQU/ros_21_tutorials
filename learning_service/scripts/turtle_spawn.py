#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy
from turtlesim.srv import Spawn

def turtle_spawn():
    # ros节点初始化
    rospy.init_node('turtle_spawn')

    # 发现/spawn服务后，创建一个服务客户端，链接名为/spawn的 service
    rospy.wait_for_service('/spawn')

    try:
        add_turtle = rospy.ServiceProxy('/spawn', Spawn)
        # 请求服务调用，输入请求数据
        response = add_turtle(2.0, 2.0, 0.0, 'turtle2')
        return response.name
    
    except rospy.ServiceException as e:
        print ('Service call failded: %s' % e)


if __name__ == "__main__":
    # 服务调用用显示调用结果
    print('spwan turtle successfully [name:%s]' % (turtle_spawn()))