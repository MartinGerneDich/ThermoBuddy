import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time

class TemperatureListener(Node):
    def __init__(self):
        super().__init__('old_temperature_listener')
        self.publisher_ = self.create_publisher(String, 'led_control', 10)
        self.serial_port = serial.Serial('COM5', 9600)  # Update with your Arduino's port
        self.serial_port.flush()  # Clear any initial garbage data

    def listen_temperature(self):
        while rclpy.ok():
            if self.serial_port.in_waiting > 0:
                # Read the temperature sent by Arduino
                temperature = self.serial_port.readline().decode('utf-8').strip()
                self.get_logger().info(f"Received temperature: {temperature}")

                # Convert the temperature to a float and decide LED state
                try:
                    temp_float = float(temperature)
                    if temp_float < 25.0:
                        self.control_leds('OFF')
                    elif 25.0 <= temp_float < 26.0:
                        self.control_leds('LOW')
                    else:
                        self.control_leds('HIGH')
                except ValueError:
                    self.get_logger().warning("Invalid temperature data received.")

            # Allow ROS2 to process any incoming messages or callbacks
            rclpy.spin_once(self, timeout_sec=0.1)  # Non-blocking, checks for ROS2 events

    def control_leds(self, state):
        # Send control commands to Arduino based on temperature
        msg = String()
        msg.data = state
        self.publisher_.publish(msg)
        self.get_logger().info(f"LED control command sent: {state}")

        self.serial_port.write((state + '\n').encode())

def main(args=None):
    rclpy.init(args=args)
    temperature_listener = TemperatureListener()
    temperature_listener.listen_temperature()

if __name__ == '__main__':
    main()
