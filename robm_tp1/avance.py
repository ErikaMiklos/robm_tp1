
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from robm_nxt_msgs.msg import MotorCommand


class Avancer(Node):

    def __init__(self):
        super().__init__('avancer')
        self.i = 0
        self.publisher_ = self.create_publisher(MotorCommand, 'nxt/command', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        #start
        if(self.i< 5) :
            msg = MotorCommand()
            msg.speed_b=0.5
            msg.speed_c=0.5
            self.publisher_.publish(msg)
            self.get_logger().info(f'Moteur B: {msg.speed_b:.2f} Vitesse du moteur C: {msg.speed_c:.2f}')
            self.i += 1
        #turn right 1
        if(self.i>= 5 & self.i<8) :
            msg = MotorCommand()
            msg.speed_b=0.6
            msg.speed_c=0.4
            self.publisher_.publish(msg)
            self.get_logger().info(f'Moteur B: {msg.speed_b:.2f} Vitesse du moteur C: {msg.speed_c:.2f}')
            self.i += 1
        #go ahead
        if(self.i>= 8 & self.i<11) :
            msg = MotorCommand()
            msg.speed_b=0.5
            msg.speed_c=0.5
            self.publisher_.publish(msg)
            self.get_logger().info(f'Moteur B: {msg.speed_b:.2f} Vitesse du moteur C: {msg.speed_c:.2f}')
            self.i += 1
        #turn right 2
        if(self.i>= 11 & self.i<14) :
            msg = MotorCommand()
            msg.speed_b=0.6
            msg.speed_c=0.4
            self.publisher_.publish(msg)
            self.get_logger().info(f'Moteur B: {msg.speed_b:.2f} Vitesse du moteur C: {msg.speed_c:.2f}')
            self.i += 1
        #go ahead
        if(self.i>= 14 & self.i<17) :
            msg = MotorCommand()
            msg.speed_b=0.5
            msg.speed_c=0.5
            self.publisher_.publish(msg)
            self.get_logger().info(f'Moteur B: {msg.speed_b:.2f} Vitesse du moteur C: {msg.speed_c:.2f}')
            self.i += 1
        #turn right 3
        if(self.i>= 17 & self.i<20) :
            msg = MotorCommand()
            msg.speed_b=0.6
            msg.speed_c=0.4
            self.publisher_.publish(msg)
            self.get_logger().info(f'Moteur B: {msg.speed_b:.2f} Vitesse du moteur C: {msg.speed_c:.2f}')
            self.i += 1
        #go back to the start point
        if(self.i>= 20 & self.i<23) :
            msg = MotorCommand()
            msg.speed_b=0.6
            msg.speed_c=0.4
            self.publisher_.publish(msg)
            self.get_logger().info(f'Moteur B: {msg.speed_b:.2f} Vitesse du moteur C: {msg.speed_c:.2f}')
            self.i += 1
        
            


def main(args=None):
    rclpy.init(args=args)

    avancer = Avancer()

    rclpy.spin(avancer)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    avancer.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()