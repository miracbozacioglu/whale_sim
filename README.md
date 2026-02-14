# 🐋 ROS 2 Whale Sim  
### Publisher & Subscriber Örneği

![ROS 2](https://img.shields.io/badge/ROS_2-Humble-blue?logo=ros&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-yellow?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

**ROS 2 düğüm haberleşmesi (Node Communication) ve Pub/Sub mimarisini simüle eden, Python tabanlı bir görselleştirme projesi.**

Bu proje, otonom sistemlerin temelini oluşturan **mesajlaşma (Publisher / Subscriber)** mantığını kavramak amacıyla geliştirilmiştir.  
Bir düğüm klavye girdilerini okuyarak veri yayınlar (**Publisher**), diğer düğüm ise bu verileri dinleyerek (**Subscriber**) ekrandaki balinayı hareket ettirir.

---

## 📂 Proje Mimarisi

Sistem, `/whale/cmd_vel` konusu (topic) üzerinden haberleşen **iki ana ROS 2 düğümünden** oluşur:

### 🟢 `whale_controller` (Publisher)
- Ok tuşları ile klavye girdilerini dinler  
- Girdileri `geometry_msgs/Twist` mesajına dönüştürür  
- Hız ve yön bilgisini yayınlar  

### 🔵 `whale_visualizer` (Subscriber)
- `/whale/cmd_vel` konusunu dinler  
- Gelen hız bilgisine göre balinanın `(x, y)` konumunu günceller  
- Hareketi `tkinter` GUI üzerinde görselleştirir  

---

## 🔄 Haberleşme Şeması
<img width="3849" height="1467" alt="Ekran Görüntüsü - 2026-02-14 12-02-35" src="https://github.com/user-attachments/assets/6f06a9d7-c0c7-4fb4-ac96-765528d584e0" />

<img width="4089" height="2560" alt="image" src="https://github.com/user-attachments/assets/30ba4e18-38f9-4c9b-8a41-3a208dcc7109" />






------

⚙️ Gereksinimler

Projeyi çalıştırmadan önce aşağıdaki bileşenlerin kurulu olması gerekir:

🖥 Sistem

İşletim Sistemi: Ubuntu 22.04 LTS (veya uyumlu Linux)

ROS Dağıtımı: ROS 2 Humble Hawksbill (Jazzy uyumlu)

Python: 3.10+

📦 Python Kütüphaneleri

sudo apt install python3-tk
pip3 install pynput


🚀 Kurulum (Build)
1️⃣ ROS 2 çalışma alanına girin
cd ~/ros2_ws/src


2️⃣ Depoyu klonlayın
https://github.com/miracbozacioglu/whale_sim.git


3️⃣ Paketi derleyin
cd ~/ros2_ws
colcon build --packages-select whale_sim


4️⃣ Ortamı kaynaklayın
source install/setup.bash




🎮 Çalıştırma

Simülasyonu çalıştırmak için iki ayrı terminal açılmalıdır.

🖥 Terminal 1 – Görselleştirici
source ~/ros2_ws/install/setup.bash
ros2 run whale_sim visualizer


🎮 Terminal 2 – Kontrolcü
source ~/ros2_ws/install/setup.bash
ros2 run whale_sim controller


📁 Dosya Yapısı

whale_sim/
├── resource/
├── test/
├── whale_sim/
│   ├── __init__.py
│   ├── whale_controller.py    # Klavye dinleyici düğümü
│   └── whale_visualizer.py    # Grafik arayüz düğümü
├── package.xml                # Paket bağımlılıkları
├── setup.py                   # Kurulum ve entry point ayarları
└── setup.cfg


🛠 Kullanılan Teknolojiler

ROS 2 (Robot Operating System) – Düğüm yönetimi & haberleşme

rclpy – ROS 2 Python istemci kütüphanesi

Tkinter – Grafik kullanıcı arayüzü

Pynput – Klavye girdisi dinleme

geometry_msgs – Hız ve yön mesajları

👤 Yazar

Miraç Bozacıoğlu
📍  Bilgisayar Mühendisliği Öğrencisi
































