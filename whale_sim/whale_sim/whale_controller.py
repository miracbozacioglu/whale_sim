import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from pynput import keyboard

class WhaleController(Node):
    def __init__(self):
        super().__init__('whale_controller')
        self.publisher_ = self.create_publisher(Twist, '/whale/cmd_vel', 10)
        
        self.msg = Twist()
        self.speed = 1.0
        
        print("Kontrolcü Başlatıldı! Yön tuşlarını kullanın. Çıkmak için ESC.")

        # Klavye dinleyicisi (Non-blocking)
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def on_press(self, key):
        try:
            if key == keyboard.Key.up:
                self.msg.angular.z = 1.0 # Yukarı
            elif key == keyboard.Key.down:
                self.msg.angular.z = -1.0 # Aşağı
            elif key == keyboard.Key.left:
                self.msg.linear.x = -1.0 # Sol
            elif key == keyboard.Key.right:
                self.msg.linear.x = 1.0 # Sağ
            elif key == keyboard.Key.esc:
                return False # Dinlemeyi durdur
            
            self.publisher_.publish(self.msg)
            
        except AttributeError:
            pass

    def on_release(self, key):
        # Tuş bırakıldığında dur
        if key in [keyboard.Key.up, keyboard.Key.down]:
            self.msg.angular.z = 0.0
        if key in [keyboard.Key.left, keyboard.Key.right]:
            self.msg.linear.x = 0.0
            
        self.publisher_.publish(self.msg)

def main(args=None):
    rclpy.init(args=args)
    node = WhaleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()