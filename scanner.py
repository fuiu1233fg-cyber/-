import sys
from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    print(f"[*] جاري فحص النطاق: {ip_range}")
    
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp = ARP(pdst=ip_range)
    packet = ether/arp
    
    result = srp(packet, timeout=3, verbose=0)[0]
    
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
        
    print("\n[+] الأجهزة النشطة المكتشفة على الشبكة:")
    print("-" * 40)
    print(f"{'عنوان IP':<20} | {'عنوان MAC'}")
    print("-" * 40)
    for device in devices:
        print(f"{device['ip']:<20} | {device['mac']}")
    print("-" * 40)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_range = sys.argv[1]
        scan_network(target_range)
    else:
        print("الاستخدام الصحيح:")
        print("python scanner.py <نطاق_الشبكة_مثل_192.168.1.0/24>")


