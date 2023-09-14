#! /usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
from learning_service.srv import Person, PersonResponse

def personCallback(req):
    # 显示请求数据
    rospy.loginfo('Person: name:%s age:%d sex:%s', req.name, req.age, req.sex)
    # 反馈数据
    return PersonResponse

def person_server():
    # ros节点初始化
    rospy.init_node('person_server')
    # 创建一个名为'/show_person'的server，注册回调函数personCallba
    s = rospy.Service('/show_person', Person, personCallback)
    # 循环等待回调函数
    print('ready to show person information.')
    rospy.spin()

if __name__ == '__main__':
    person_server()
