Project Setup and Environment Instructions

This guide provides step-by-step instructions for setting up the environment and running the project. The project is based on ROS 2 Jazzy and requires an Arduino for serial communication.
1. Prerequisites

    Install ROS 2 Jazzy
    Follow the official instructions for ROS 2 Jazzy installation on Windows:
    ROS 2 Jazzy Installation Guide.
    Install ROS 2 Jazzy at C:\dev\ros2_jazzy (or any preferred path).

    Install Arduino IDE
        Download and install the Arduino IDE from Arduino's official website.
        Upload the corresponding Arduino project (included in this repository) to your Arduino board.

    Install colcon
    Ensure you have colcon installed for building the ROS 2 workspace:

    pip install -U colcon-common-extensions

2. Setting up the Workspace

    Clone this repository or download the project into a workspace folder.
    Example location: C:\dev\ros2_ws

    Open a command prompt and navigate to the workspace directory:

cd C:\dev\ros2_ws

Source the ROS 2 Jazzy environment:

call C:\dev\ros2_jazzy\local_setup.bat

Source the project workspace:

    call install\local_setup.bat

3. Build the Project

In the workspace directory (C:\dev\ros2_ws), build the project using colcon:

colcon build --merge-install

4. Run the Nodes

After building the workspace, you can run the ROS 2 nodes as follows:

    Computation Node:

ros2 run my_project computation_node

LED Control Node:

ros2 run my_project led_control_node

Temperature Listener Node:

    ros2 run my_project temperature_listener

5. Arduino Requirements

    Connect your Arduino board to the PC via USB.
    Upload the provided Arduino project to the board using the Arduino IDE.
        The Arduino project is located in the arduino/ folder of this repository.
    Verify that a serial connection is established between the Arduino and the PC.

6. Notes

    Ensure you source both local_setup.bat files in the correct order after every restart:
        First: C:\dev\ros2_jazzy\local_setup.bat
        Then: install\local_setup.bat inside your workspace.
    The Arduino must remain connected for proper communication with the ROS nodes.
