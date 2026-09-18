import os
import threading
from flask import Flask

Ini server mini agar Render tidak mematikan bot
app = Flask(name)
@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    # Menjalankan server web di port 10000 (aturan dari Render)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

def run_bot():
    print("Bot Telegram siap!")
    # MASUKKAN KODE BOT TELEGRAM ANDA DI BAWAH SINI
    # Contoh: import kode_bot_anda_yang_lama()

if name == "main":
    # Menjalankan web server dan bot secara bersamaan
    threading.Thread(target=run_web).start()
    run_bot()
