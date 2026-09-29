import time, requests

TOKEN = "8758727584:AAFkQAN6X83xWwq1Im7l79FPpPatj433uSQ"
CHAT_ID = ""
PAXG_URL = "https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT"

def send(msg):
    try:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}", timeout=10)
    except Exception as e:
        print(e)

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
            send(f"🔴 H DUSUS - Cift Tepe geldi! Fiyat: {price}")
        elif price <= 4145:
            send(f"🔵 L CIKIS - Cift Dip geldi! Fiyat: {price}")
    except Exception as e:
        print(e)

cid = get_chat_id_auto()
if cid:
    CHAT_ID = str(cid)
    send("✅ ali_gold_816_bot 7/24 calismaya basladi - py3 arka planda acik kanka!")
    print(f"Chat ID: {CHAT_ID}")
else:
    print("Telegram'da @ali_gold_816_bot'a /start yaz")

while True:
    check()
    time.sleep(60)
