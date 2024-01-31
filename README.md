# ROS2 Tello Driver

## About The Project
ROS2 driver to control Tello drones based on Tello SDK 2.0. Features include: status and video stream, action server for processing commands (takeoff, land, etc), connect to wifi access points, and swarm control.

## Getting Started
The driver has been tested on Ubuntu 22.04 with ROS2 Humble.

### Prerequisites
* ROS2 Humble
* Numpy
* h264decoder ([link to repo](https://github.com/DaWelter/h264decoder))

### Installation
To install the Tello driver:

```
mkdir tello_ws && cd tello_ws
mkdir src && cd src
git clone https://github.com/MRT-Codebase/ros2_tello_driver.git
colcon build
source install/setup.bash
```

## Usage
Run by connecting to drone access point
```
ros2 launch tello_driver single_launch.py
```

To change access point, first connect to the drone then modify the ssid and password in **change_ap_launch.py** in the **tello_driver** package, then run:
```
ros2 launch tello_driver change_ap_launch.py
```

To connect to the drone through your own access point, make sure your PC is connected to the access point, then run:
```
ros2 launch tello_driver ap_single_launch.py
```

To control a swarm of drones: (you can add more nodes to the launch file depending on the number of drones connected)
```
ros2 launch tello_driver ap_multiple_launch.py
```

## Contact
Kousheek Chakraborty - kousheekc@gmail.com

Project Link: [https://github.com/MRT-Codebase/ros2_tello_driver](https://github.com/MRT-Codebase/ros2_tello_driver)

