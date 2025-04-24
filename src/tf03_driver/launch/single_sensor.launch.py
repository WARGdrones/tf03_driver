from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="tf03_driver",
                executable="tf03_node",
                name="tf03_driver",
                namespace="tf03_driver",
                output="screen",
                parameters=[
                    {
                        "sensor_frame": ["front"],
                        "sensor_interface": "serial",
                        "serial_port": "/dev/ttyUSB0",
                    }
                ],
            )
        ]
    )
