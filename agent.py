import platform
import socket
import time
import requests

SERVER_URL = "http://127.0.0.1:8080/api/beacon"

def get_device_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    system_info = f"{platform.system()} {platform.release()}"
    
    payload = {
        "id": f"DEV-{socket.getnode()}",
        "device_name": system_info,
        "ip_address": ip_address,
        "status": "نشط"
    }
    return payload

def start_beaconing():
    print("[-] Initializing secure beacon...")
    while True:
        try:
            data = get_device_info()
            response = requests.post(SERVER_URL, json=data, timeout=5)
            if response.status_code == 200:
                print("[+] Beacon sent successfully.")
        except requests.exceptions.RequestException:
            pass
        time.sleep(10)

if __name__ == "__main__":
    start_beaconing()

