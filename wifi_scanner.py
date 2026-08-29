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
