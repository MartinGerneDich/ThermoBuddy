import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class LEDControlNode(Node):
    def __init__(self):
        super().__init__('led_control_node')
        self.subscription = self.create_subscription(
            String,
            'computed_temperature',
            self.listener_callback,
            10
        )
        self.publisher_ = self.create_publisher(String,'led_control_command',10)
    

    def listener_callback(self, msg):
        try:
            # Parse the computed temperature
            temperature_celsius = float(msg.data)
            self.get_logger().info(f"Received computed temperature: {temperature_celsius:.2f}")
            
            # Control LEDs based on temperature
            if temperature_celsius < 23.0:
                self.control_leds('COLD')
            elif 23.0 <= temperature_celsius < 25.0:
                self.control_leds('WARM')
            else:
                self.control_leds('HOT')

        except ValueError:
            self.get_logger().warning("Invalid temperature data received.")

    def control_leds(self, state):
        # Send control commands to Arduino based on the LED state
        msg = String()
        msg.data = state
        self.publisher_.publish(msg)
        #self.serial_port.write((state + '\n').encode())
        self.get_logger().info(f"LED control command sent: {state}")

def main(args=None):
    rclpy.init(args=args)
    led_control_node = LEDControlNode()
    rclpy.spin(led_control_node)

if __name__ == '__main__':
    main()
