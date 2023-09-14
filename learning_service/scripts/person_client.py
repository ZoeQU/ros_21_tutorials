#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import rospy
from learning_service.srv import Person, PersonRequest


def person_client():
    # ros节点初始化
    rospy.init_node('person_client')
    # 发现服务后，创建服务客户端，连接名为 /show_person 的 service
    rospy.wait_for_service('/show_person')

    try:
        person_client = rospy.ServiceProxy('/show_person', Person)
        # 请求服务调用，输入请求数据
        response = person_client('Tom', 20, 'male')
        return response.result
    
    except rospy.ServiceException as e:
        print('service call failed: %s' % e)


if __name__ == '__main__':
    # 服务调用并显示调用结果
    print('show person result: %s' % (person_client()))