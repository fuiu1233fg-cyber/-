import requests

def track_target(ip_address=""):
    try:
        url = f"http://ip-api.com/json/{ip_address}"
        response = requests.get(url)
        data = response.json()
        
        if data['status'] == 'success':
            print("\n[+] تم استخراج البيانات بنجاح:")
            print(f"IP: {data.get('query')}")
            print(f"الدولة: {data.get('country')} ({data.get('countryCode')})")
            print(f"المنطقة / المحافظة: {data.get('regionName')}")
            print(f"المدينة: {data.get('city')}")
            print(f"الرمز البريدي: {data.get('zip')}")
            print(f"خط العرض (Latitude): {data.get('lat')}")
            print(f"خط الطول (Longitude): {data.get('lon')}")
            print(f"مزود الخدمة (ISP): {data.get('isp')}")
            print(f"المنظمة: {data.get('org')}")
        else:
            print("[-] فشل في تحديد الموقع، الأيبي غير صالح أو غير متاح.")
            
    except Exception as e:
        print(f"[-] حدث خطأ أثناء الاتصال: {e}")

if __name__ == "__main__":
    target = input("أدخل عنوان IP (اضغط Enter لفحص جهازك الحالي): ").strip()
    track_target(target)

