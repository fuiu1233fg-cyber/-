#!/bin/bash
echo "[+] تحديث حزم Termux وتثبيت الأدوات الأساسية..."
pkg update && pkg upgrade -y
pkg install python git libnl libpcap tcpdump -y
echo "[+] تثبيت مكتبة Scapy للتحكم في الحزم الشبكية..."
pip install scapy
echo "[+] إنشاء سكريبت فحص الشبكات المحيطة..."
cat << 'EOF' > wifi_scanner.py
from scapy.all import *
import sys

def packet_handler(packet):
    if packet.haslayer(Dot11Beacon):
        ssid = packet[Dot11Elt].info.decode('utf-8', errors='ignore')
        bssid = packet[Dot11].addr2
        channel = ord(packet[Dot11Elt:3].info) if packet[Dot11Elt:3] else "N/A"
        print(f"[+] الشبكة: {ssid} | BSSID: {bssid} | القناة: {channel}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[-] الاستخدام: python wifi_scanner.py <INTERFACE>")
        sys.exit(1)
    
    interface = sys.argv[1]
    print(f"[*] جارٍ بدء فحص الشبكات عبر الواجهة {interface}...")
    sniff(iface=interface, prn=packet_handler, timeout=20)
EOF

echo "[+] تم إعداد السكريبت بنجاح."
echo "[*] لتشغيل الفحص، استخدم الأمر التالي (يتطلب صلاحيات Root):"
echo "su"
echo "python wifi_scanner.py wlan0"
pkg install tcpdump python-pip -y
pip install scapy
su
python wifi_scanner.py wlan0
pkg install python python-pip -y
pip install scapy
import sys
from scapy.all import ARP, Ether, srp
def scan_network(ip_range):
if __name__ == "__main__":;     if len(sys.argv) > 1:
nano scanner.py
python scanner.py 192.168.1.0/24
import socket
import sys
import threading
def scan_ip(ip):
def main():
if __name__ == "__main__":;     main()
cat << 'EOF' > net_scan_socket.py
import socket
import sys
import threading
def scan_ip(ip):
def main():
if __name__ == "__main__":;     main() EOF
printf "import socket, sys, threading\n\ndef scan_ip(ip):\n    try:\n        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n        s.settimeout(0.3)\n        if s.connect_ex((ip, 80)) == 0:\n            print(f'[+] جهاز نشط: {ip}')\n        s.close()\n    except: pass\n\nif __name__ == '__main__':\n    base = sys.argv[1] if len(sys.argv) > 1 else '192.168.1'\n    threads = [threading.Thread(target=scan_ip, args=(f'{base}.{i}',))\n for i in range(1, 255)]\n    [t.start() for t in threads]\n    [t.join() for t in threads]\n    print('[+] انتهى الفحص.')\n" > net_scan_socket.py
nano net_scan_socket.py
python net_scan_socket.py 192.168.1
ifconfig
import requests
import json
def track_target(ip_address=""):
if __name__ == "__main__":;     target = input("أدخل عنوان IP (اضغط Enter لفحص جهازك الحالي): ").strip()
nano tracker.py
python3 tracker.py
pkg update && pkg install python-pip -y
pip install requests
python3 tracker.py
pkg update && pkg install wget -y
# تحميل نسخة ngrok المناسبة لـ Termux (أو تثبيتها عبر الحزم المتاحة)
nano web_tracker.py
python3 web_tracker.py
sed -i 's/print(\[+\] تم اصطياد الضحية بنجاح!)/print("[+] تم اصطياد الضحية بنجاح!")/g' web_tracker.py
python3 web_tracker.py
