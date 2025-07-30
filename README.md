# Autonomous Mobile Robot

This project is focused on developing a fully functional Autonomous Mobile Robot (AMR). The system integrates multiple hardware and software components for autonomous navigation, mapping, and perception.

The robot is driven by two 100 RPM Johnson DC motors equipped with quadrature encoders for accurate odometry feedback. The motor control is managed by a BTS-7960 high-power motor driver, capable of handling high current loads. Power is supplied through a 14.8V lithium-ion battery, and a buck converter is used to step down the voltage to the required level for motor operation.

The main microcontroller is the ESP32-S3, responsible for real-time sensor data processing and motor actuation. For perception and localization, the robot uses an RP-LIDAR (range up to 6 meters) for obstacle detection and mapping, along with an MPU-6050 IMU for orientation and motion tracking.

The core computational tasks — such as path planning, SLAM, and control algorithms are handled by the Raspberry Pi 4, running Ubuntu 22.04. It serves as the central processing unit, managing high-level logic and coordinating with the ESP32.

Additionally, a 10,000 mAh 20W power bank is used to power the Raspberry Pi and other low-voltage electronics separately from the motors. The system combines onboard vision, sensor fusion, and motor control to navigate and interact with its environment without human intervention.

## Key Features:
- Autonomous navigation using LIDAR and IMU data
- Real-time odometry with quadrature encoders
- ESP32 used for low-level motor and sensor control 
- ROS 2 Humble integration (if applicable)
- Remote monitoring and control via SSH or web interface

## 📦 Hardware Components
| Component          | Model / Specs                                | Quantity |
|--------------------|-----------------------------------------------|----------|
| Motors             | 100 RPM Johnson DC motors (with encoders)     | 2        |
| Motor Driver       | BTS-7960                                       | 2        |
| Microcontroller    | ESP32-S3                                       | 1        |
| Microprocessor     | Raspberry Pi 4                                 | 1        |
| Power Supply       | 14.8V Li-ion Battery (4000mAh)                 | 1        |
| DC-DC Converter    | LM2596 Buck Converter (5V for encoders)        | 1        |
| DC-DC Converter    | Generic Buck Converter (12V for motor supply)  | 1        |
| LIDAR              | RP-LIDAR (6m range)                            | 1        |
| IMU                | MPU-6050                                       | 1        |
| Auxiliary Power    | 20W 10,000mAh Power Bank (for Raspberry Pi)    | 1        |

## 🗂 Directory Structure
```
my_amr/
├── config/
│   ├── drive_amr_rviz.rviz
│   ├── empty.yaml
│   ├── gazebo_params.yaml
│   ├── my_controllers.yaml
│   └── view_amr_rviz.rviz
│
├── description/
│   ├── camera.xacro
│   ├── gazebo_control.xacro
│   ├── inertial_macros.xacro
│   ├── lidar.xacro
│   ├── robot.urdf.xacro
│   ├── robot_core.xacro
│   └── ros2_control.xacro
│
├── launch/
│   ├── launch_robot.launch.py
│   ├── launch_sim.launch.py
│   └── rsp.launch.py
│
├── worlds/
│   ├── empty.world
│   └── wall.world
├── CMakeLists.txt
│
├── LICENSE.md
├── README.md
├── package.xml

``` 

## 💻 Software Stack
- Ubuntu 22.04
- ROS 2 Humble
- Python 3 / C++
- Arduino IDE
- Serial & I2C communication protocols


<img width="500" height="600" alt="image" align="center" src="https://github.com/user-attachments/assets/f3557f0f-b83c-42b9-84e1-36b483d27081" />
