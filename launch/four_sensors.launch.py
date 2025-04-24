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
                        "can_transmit_id": [3, 4, 5, 6],
                        "sensor_frame": [
                            "front_left",
                            "front_right",
                            "rear_left",
                            "rear_right",
                        ],
                        "sensor_interface": "can",
                        "can_device": "benewake_can",
                    }
                ],
            )
        ]
    )
