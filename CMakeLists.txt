cmake_minimum_required(VERSION 2.8.3)
project(auto_ipc)

find_package(catkin REQUIRED COMPONENTS
  rospy
  actionlib
  actionlib_msgs
  std_msgs
)

add_action_files(
  DIRECTORY action
  FILES ipc.action
)

generate_messages(
  DEPENDENCIES actionlib_msgs std_msgs
)

catkin_package(
  CATKIN_DEPENDS rospy actionlib actionlib_msgs std_msgs
)
