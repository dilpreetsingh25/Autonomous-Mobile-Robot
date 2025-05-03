import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    package_name = 'my_amr'

    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory(package_name),
                'launch','rsp.launch.py')
            ),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('gazebo_ros'),
                'launch','gazebo.launch.py')
            ),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'my_amr',
            '-topic', 'robot_description'],
        output='screen'
    )

    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity
    ])
# This launch file includes the robot state publisher (rsp) and the Gazebo simulation environment.
# It also spawns the robot in the Gazebo environment using the robot description from the URDF file.
# The robot is spawned at the origin (0, 0, 0) with no rotation.
# The launch file uses the `IncludeLaunchDescription` action to include the rsp and Gazebo launch files.
# The `spawn_entity` node is used to spawn the robot in the Gazebo environment.
# The `use_sim_time` argument is set to true to use simulated time in the Gazebo environment.
# The `robot_description` topic is used to pass the robot description to the Gazebo environment.
# The `output` argument is set to 'screen' to display the output in the terminal.
# The `arguments` list contains the arguments to be passed to the `spawn_entity` node.
# The `-entity` argument specifies the name of the robot in the Gazebo environment.
# The `-topic` argument specifies the topic to be used for the robot description.
# The `rsp` launch file is included first to ensure that the robot description is available before spawning the robot.
# The `gazebo` launch file is included second to start the Gazebo simulation environment.
# The `spawn_entity` node is included last to spawn the robot in the Gazebo environment.
# The launch file uses the `os` module to get the package share directory for the `my_amr` and `gazebo_ros` packages.
# The `ament_index_python` package is used to get the package share directory.
# The `launch` module is used to create the launch description and include the launch files.
# The `launch_ros` module is used to create the `spawn_entity` node.
# The `PythonLaunchDescriptionSource` class is used to specify the launch file to be included.
# The `IncludeLaunchDescription` class is used to include the launch files.
# The `Node` class is used to create the `spawn_entity` node.
# The `LaunchDescription` class is used to create the launch description.
# The `launch_arguments` parameter is used to pass arguments to the included launch files.