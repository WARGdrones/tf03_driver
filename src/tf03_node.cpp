#include <TF03.h>

#include <rclcpp/rclcpp.hpp>

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<TF03>("tf03_node");
  RCLCPP_INFO(node->get_logger(), "Init TF03 object");
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
