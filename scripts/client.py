#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import actionlib

from auto_ipc.msg import ipcAction, ipcGoal

def feedback_cb(feedback):
    rospy.loginfo(f"Progress: {feedback.progress}")

if __name__ == "__main__":
    rospy.init_node("ipc_client")

    client = actionlib.SimpleActionClient("ipc_action", ipcAction)
    rospy.loginfo("Waiting for action server...")
    client.wait_for_server()

    goal = ipcGoal(target=5, timeout=10.0)
    client.send_goal(goal, feedback_cb=feedback_cb)

    client.wait_for_result()
    result = client.get_result()
    rospy.loginfo(f"Result: success={result.success}, message={result.message}")
