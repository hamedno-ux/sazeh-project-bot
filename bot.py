import os
import requests
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    print(response.status_code, response.text)

if __name__ == "__main__":
    today = datetime.now().strftime("%Y/%m/%d")
    
    message = f"""📋 *گزارش و بررسی روزانه پروژه‌ها*
📅 تاریخ: {today}

لطفاً وضعیت پروژه‌های خود را اعلام کنید:

۱. پیشرفت امروز چقدر بوده؟
۲. آیا مشکلی وجود دارد؟
۳. برای فردا چه برنامه‌ای دارید؟

اگر مشکلی دارید همین‌جا بنویسید تا پیگیری شود.
"""
    send_message(message)
    print("پیام با موفقیت ارسال شد")
