import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ComputationNode(Node):
    def __init__(self):
        super().__init__('computation_node')
        self.subscription = self.create_subscription(
            String,
            'temperature_data',
            self.listener_callback,
            10
        )
        self.publisher_ = self.create_publisher(String, 'computed_temperature', 10)

    def listener_callback(self, msg):
        try:
            # Convert temperature
            sensorData = float(msg.data)
            voltage = (sensorData /1024.0) * 5.0
            temperature_celsius = (voltage - .5) * 100
            
            # Publish the computed temperature to the next node
            computed_temp_msg = String()
            computed_temp_msg.data = str(temperature_celsius)
            self.publisher_.publish(computed_temp_msg)
            self.get_logger().info(f"Computed temperature (Celsius): {temperature_celsius:.2f}")

        except ValueError:
            self.get_logger().warning("Invalid temperature data received.")

def main(args=None):
    rclpy.init(args=args)
    computation_node = ComputationNode()
    rclpy.spin(computation_node)

if __name__ == '__main__':
    main()
