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
    
    message = f"""📋 *گزارش دو روز یکبار پروژه‌ها*
📅 تاریخ: {today}

لطفاً یکی از گزینه‌های زیر را انتخاب کنید و پاسخ دهید:

────────────────────
🆕 *۱. معرفی پروژه جدید*
اگر پروژه جدیدی شروع شده، این اطلاعات را بنویسید:
• نام پروژه:
• تاریخ شروع:
• تاریخ تحویل تقریبی:
• مسئول پروژه:
• وضعیت فعلی:
• برنامه زمانی (تایم‌لاین) مختصر:

────────────────────
🔄 *۲. پیگیری پروژه‌های موجود*
برای هر پروژه فعال بنویسید:
• نام پروژه:
• درصد پیشرفت:
• کارهای انجام‌شده در ۴۸ ساعت گذشته:
• مشکلات و موانع:
• برنامه ۴۸ ساعت آینده:

────────────────────
⚠️ اگر مشکلی فوری وجود دارد، همین‌جا با ذکر نام پروژه اعلام کنید.

"""
    send_message(message)
    print("پیام با موفقیت ارسال شد")
