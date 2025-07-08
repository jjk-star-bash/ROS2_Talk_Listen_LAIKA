#!/usr/bin/env python3 
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber(Node):
    def __init__(self):
       
        super().__init__("laika_listener")
        self.subscription = self.create_subscription(String, "topic", self.listener_callback, 10) #note how its called a subscription not a subscriber 
        self.subscription #prevents unused var alert 
    '''No timer is needed since the subscriber simply respinses to publications, so it is in a sense always on, and has no tick-rate'''

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data) #logger to express data hearing on execution

def main (args=None):
    rclpy.init(args=args) #initialize ros comms
    node = MinimalSubscriber() #object orientyed node created
    rclpy.spin(node) #subs need to spin to collect info continuously with talker 
    rclpy.shutdown() 

if __name__ == "__main__":
    main()
