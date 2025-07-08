#!usr/bin/env python3
import rclpy
from rclpy.node import Node #inheritable class
from std_msgs.msg import String #Publishing text to a topic class of strings


class MinimalPublisher(Node): #my own class (oriented programming) inherits all functionalities
     
    def __init__(self): #constructor
        super().__init__("laika_talker") # where you put the node name, name in ROS graph
        self.publisher = self.create_publisher(String, "topic", 10) #Creats itself and defines the topic to publish to as "topic"
        
        '''create_publisher declares that the node publishes messages of type String 
        (imported from the std_msgs.msg module), over a topic named topic, and that the “queue size” is 10.'''
        
        timer_period = 0.5 # Sec.
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0

    '''timer_callback creates a message with the counter value appended'''

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello world from the Laika talking node! Itteration: %d' %self.count
        self.publisher.publish(msg)
        self.get_logger().info ('PUBLISHING: "%s"' %msg.data)
        self.count += 1    


def main(args=None):
    rclpy.init(args=args) #initializes ros2 communication (first line)
    node = MinimalPublisher() #node is now inside the main   
    rclpy.spin(node) #keeps node alive

    rclpy.shutdown() #shuts down ros2 communication (last line)


if __name__ == "__main__":
    main()