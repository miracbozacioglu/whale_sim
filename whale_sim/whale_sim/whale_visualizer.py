import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import tkinter as tk

class WhaleVisualizer(Node):
    def __init__(self):
        super().__init__('whale_visualizer')
        
        # Abone olunan konu (Subscriber)
        self.subscription = self.create_subscription(
            Twist,
            '/whale/cmd_vel',
            self.listener_callback,
            10)
        
        # Balinanın hızı
        self.vel_x = 0.0
        self.vel_y = 0.0

        # Arayüz (GUI) Ayarları
        self.root = tk.Tk()
        self.root.title("ROS 2 Yüzen Balina Simülasyonu")
        self.root.geometry("600x400")
        
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="lightblue")
        self.canvas.pack()

        # Balinayı çizelim (Basit bir oval ve kuyruk)
        # x, y koordinatları
        self.x = 300
        self.y = 200
        self.whale_body = self.canvas.create_oval(self.x-40, self.y-20, self.x+40, self.y+20, fill="blue")
        self.whale_tail = self.canvas.create_polygon(self.x+35, self.y, self.x+60, self.y-15, self.x+60, self.y+15, fill="blue")

        # GUI güncelleme döngüsü (100ms'de bir)
        self.root.after(100, self.update_gui)

    def listener_callback(self, msg):
        # Mesaj geldiğinde hız değişkenlerini güncelle
        # Arayüzde Y ekseni aşağı doğru arttığı için Y'yi ters alabiliriz veya düz mantık kurabiliriz.
        # Burada: Linear X -> Sağ/Sol, Angular Z -> Yukarı/Aşağı (Basitlik olsun diye Twist'i böyle kullanıyoruz)
        self.vel_x = msg.linear.x
        self.vel_y = msg.angular.z # 2D basit hareket için angular.z'yi Y ekseni gibi kullanacağım

    def update_gui(self):
        # ROS 2 callbacklerini işle (Spin once)
        rclpy.spin_once(self, timeout_sec=0)
        
        # Pozisyonu güncelle
        self.x += self.vel_x * 5  # Hız çarpanı
        self.y -= self.vel_y * 5  # Y ekseni tkinter'da ters (aşağısı pozitif), o yüzden (-)
        
        # Sınır kontrolü (Ekrandan çıkmasın)
        self.x = max(50, min(550, self.x))
        self.y = max(50, min(350, self.y))

        # Çizimi taşı
        self.canvas.coords(self.whale_body, self.x-40, self.y-20, self.x+40, self.y+20)
        self.canvas.coords(self.whale_tail, self.x+35, self.y, self.x+60, self.y-15, self.x+60, self.y+15)

        # Döngüyü tekrarla
        self.root.after(50, self.update_gui)

def main(args=None):
    rclpy.init(args=args)
    visualizer_node = WhaleVisualizer()
    visualizer_node.root.mainloop() # Tkinter ana döngüsü
    
    visualizer_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()