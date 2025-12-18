#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import actionlib

from auto_ipc.msg import ipcAction, ipcFeedback, ipcResult

class IPCActionServer:
    def __init__(self):
        self.server = actionlib.SimpleActionServer(
            "ipc_action",
            ipcAction,
            execute_cb=self.execute_cb,
            auto_start=False
        )
        self.server.start()
        rospy.loginfo("ipc server started")

    def execute_cb(self, goal):
        rospy.loginfo(f"Received goal: target={goal.target}, timeout={goal.timeout}")

        feedback = ipcFeedback()
        result = ipcResult()

        rate = rospy.Rate(1)
        for i in range(0, goal.target + 1):
            if self.server.is_preempt_requested():
                rospy.logwarn("Action preempted")
                self.server.set_preempted()
                return

            feedback.progress = i
            self.server.publish_feedback(feedback)
            rate.sleep()

        result.success = True
        result.message = "Completed successfully"
        self.server.set_succeeded(result)

if __name__ == "__main__":
    rospy.init_node("ipc_action_server")
    IPCActionServer()
    rospy.spin()
