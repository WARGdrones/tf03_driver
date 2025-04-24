cmake_minimum_required(VERSION 3.5)
project(tf03_driver)



# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)


find_package(PkgConfig)
pkg_check_modules(SERIAL libserial)

if(SERIAL_VERSION VERSION_LESS 1.0.0)
  add_definitions(-DLIBSERIAL_0_X)
endif()

# Include directories
include_directories(
  include

  ${SERIAL_INCLUDE_DIRS}
)
  # Add executable
add_executable(tf03_node src/tf03_node.cpp src/TF03.cpp)

# Link libraries
ament_target_dependencies(tf03_node rclcpp std_msgs sensor_msgs)

# Link LibSerial library
target_link_libraries(tf03_node
  ${catkin_LIBRARIES}
  ${SERIAL_LDFLAGS}

)

# Install targets
install(TARGETS tf03_node
  DESTINATION lib/${PROJECT_NAME})

# Install launch files
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/launch)

# Ament package
ament_package()
