import socket
import sys
import threading

def scan_ip(ip):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        if s.connect_ex((ip, 80)) == 0:
            print(f"[+] جهاز نشط: {ip}")
        s.close()
    except:
        pass

if __name__ == '__main__':
    base = sys.argv[1] if len(sys.argv) > 1 else '192.168.1'
    print(f"[*] جاري فحص النطاق {base}.1 إلى {base}.254 ...")
    threads = [threading.Thread(target=scan_ip, args=(f'{base}.{i}',)) for i in range(1, 255)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("[+] انتهى الفحص.")


