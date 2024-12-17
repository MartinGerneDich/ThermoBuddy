import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class TemperatureListener(Node):
    def __init__(self):
        super().__init__('temperature_listener')
        self.publisher_ = self.create_publisher(String, 'temperature_data', 10)
        self.subscription = self.create_subscription(
            String,
            'led_control_command',
            self.listener_callback,
            10
        )
        self.serial_port = serial.Serial('COM5', 9600)  
        self.serial_port.flush()  

    def listener_callback(self, msg):
        state = msg.data
        self.get_logger().info(f"Received LED control command:{state}")
        self.send_to_arduino(state)

    def listen_temperature(self):
        while rclpy.ok():
            if self.serial_port.in_waiting > 0:
                # Read the temperature sent by Arduino
                temperature = self.serial_port.readline().decode('utf-8').strip()
                self.get_logger().info(f"Received temperature: {temperature}")
                
                # Publish the temperature data to a topic
                msg = String()
                msg.data = temperature
                self.publisher_.publish(msg)
                self.get_logger().info(f"Temperature data sent to /temperature_data: {temperature}")

            rclpy.spin_once(self, timeout_sec=0.1)

    def send_to_arduino(self, state):
        # Send the LED control command to the Arduino over serial
        self.serial_port.write((state + '\n').encode())
        self.get_logger().info(f"Sent LED control command to Arduino: {state}")

def main(args=None):
    rclpy.init(args=args)
    temperature_listener = TemperatureListener()
    temperature_listener.listen_temperature()

if __name__ == '__main__':
    main()
