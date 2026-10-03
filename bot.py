import os
import requests
from datetime import datetime

# خواندن اطلاعات از Secrets
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # کلید رایگان هوش مصنوعی

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

def generate_report():
    # این بخش با هوش مصنوعی گزارش می‌سازه
    prompt = f"""
تو یک مدیر پروژه هستی. امروز تاریخ {datetime.now().strftime('%Y-%m-%d')} است.
یک گزارش کوتاه و حرفه‌ای برای گروه پروژه بنویس که شامل این بخش‌ها باشد:
1. درخواست آپدیت وضعیت پروژه‌ها
2. درخواست اعلام مشکلات
3. یادآوری بررسی روزانه
لحن رسمی ولی دوستانه باشه و به فارسی بنویس.
"""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=data
    )
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "خطا در تولید گزارش. لطفا وضعیت پروژه‌ها را اعلام کنید."

if __name__ == "__main__":
    report = generate_report()
    send_message(report)
    print("گزارش ارسال شد")
