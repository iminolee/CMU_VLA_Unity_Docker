#!/bin/bash
set -e

# ROS Noetic Environment Setup
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source /opt/ros/noetic/setup.bash

echo "==== CMU VLA Challenge Unity Docker Ready ===="

cd /workspace

exec bash