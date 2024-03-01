#!/usr/bin/env python3
import rospy

if __name__ == "main":
    rospy.init_node("vann_test")

    rospy.loginfo("test_hello")
    rospy.logwarn("warn")
    rospy.logerr("error")

    rospy.sleep(1.0)

    rospy.loginfo("End")
