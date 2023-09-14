#! /usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
import threading, time
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse

pubCommand = False
turtle_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

def command_thread():
    while True:
        if pubCommand:
            vel_msg = Twist()
            vel_msg.linear.x = 0.5
            vel_msg.angular.z = 0.2
            turtle_vel_pub.publish(vel_msg)
        
        time.sleep(0.1)

def commandCallback(req):
    global pubCommand
    pubCommand = bool(1-pubCommand)
    
    # 显示请求数据
    rospy.loginfo('publish turtle velocity command! [%d]', pubCommand)
    # 反馈数据
    return TriggerResponse(1, 'change turtle command state!')

def turtle_command_server():
    # ros节点初始化
    rospy.init_node('turtle_command_server')

    # 创建一个名为 /turtle_command的 server,注册回调函数 commandCallback
    s = rospy.Service('/turtle_command', Trigger, commandCallback)
    
    # 循环等待回调函数
    print('ready to receive turtle command.')

    my_thread = threading.Thread(target=command_thread)
    my_thread.start()
    # threading.Thread.start(command_thread)
    rospy.spin()


if __name__ == "__main__":
    turtle_command_server()