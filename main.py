
import time, requests, os, threading
from http.server import BaseHTTPRequestHandler, HTTPServer

TOKEN = "8758727584:AAFkQAN6X83xWwq1Im7l79FPpPatj433uSQ"
CHAT_ID = ""
PAXG_URL = "https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT"

def run_fake_server():
    port = int(os.environ.get("PORT", 10000))
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Bot 7/24 calisiyor kanka!")
    httpd = HTTPServer(("0.0.0.0", port), Handler)
    httpd.serve_forever()

threading.Thread(target=run_fake_server, daemon=True).start()

def send(msg):
    if not CHAT_ID: return
    try:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}", timeout=10)
    except: pass

def get_chat_id_auto():
    try:
        r = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates", timeout=10).json()
        if r.get("result"):
            return r["result"][-1]["message"]["chat"]["id"]
    except: pass
    return None

def check():
    try:
        price = float(requests.get(PAXG_URL, timeout=10).json()['price'])
        print(f"GOLD {price}")
        if price >= 4161:
            send(f"🔴 H DUSUS - Cift Tepe! {price}")
        elif price <= 4145:
            send(f"🔵 L CIKIS - Cift Dip! {price}")
    except Exception as e:
        print(e)

cid = get_chat_id_auto()
if cid:
    CHAT_ID = str(cid)
    print(f"Chat ID bulundu: {CHAT_ID}")
    send("✅ Bot 7/24 Render'da basladi! py3 kapansa bile calisir!")

while True:
    check()
    time.sleep(60)
