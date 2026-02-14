# 🐋 ROS 2 Whale Sim

**ROS 2 düğüm haberleşmesi (Node Communication) ve Pub/Sub mimarisini simüle eden, Python tabanlı görselleştirme projesi.**

Bu proje, bir otonom sistemin temeli olan "kontrolcü" ve "görselleştirici" yapılarını basit bir örnekle açıklar. `whale_controller` düğümü klavye verilerini alır ve yayınlar (Publish), `whale_visualizer` düğümü ise bu verileri dinleyerek (Subscribe) `tkinter` arayüzündeki balinayı hareket ettirir.

![ROS 2 Badge](https://img.shields.io/badge/ROS%202-Humble-blue)
![Language](https://img.shields.io/badge/Language-Python%203-yellow)

## 📂 Proje Mimarisi

Sistem iki ana düğümden oluşur:

1.  **`whale_visualizer` (Subscriber):**
    * Arayüzü oluşturur (Tkinter).
    * `/whale/cmd_vel` konusunu dinler.
    * Gelen hız verisine göre balinanın konumunu günceller.
2.  **`whale_controller` (Publisher):**
    * Klavye ok tuşlarını dinler (Pynput).
    * Yön verilerini `geometry_msgs/Twist` mesajına çevirir.
    * `/whale/cmd_vel` konusuna yayınlar.

**Haberleşme Şeması:**
```mermaid
[Klavye Girdisi] --> (whale_controller) --[/whale/cmd_vel]--> (whale_visualizer) --> [Grafik Arayüz]

''''''

⚙️ Gereksinimler
Bu projeyi çalıştırmak için aşağıdaki yazılımların yüklü olması gerekir:

💡 Ubuntu 22.04 (veya uyumlu bir Linux dağıtımı)

💡 ROS 2 Humble (veya Jazzy)

💡 Python 3


'''''































