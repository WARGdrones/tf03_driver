#!/bin/bash
set -e

if [ -f install/setup.bash ]; then source install/setup.bash; fi
colcon test --merge-install
colcon test-result --verbose


# to run test with output, run:
# launch_test src/<package_name>/test/<test_name>.py
