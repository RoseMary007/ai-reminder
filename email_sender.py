import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(to_email, task, time):
    msg = EmailMessage()
    msg["Subject"] = "⏰ Task Reminder"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email

    msg.set_content(f"""
Hello 👋

This is your task reminder:

📝 Task: {task}
⏰ Time: {time}

Stay productive 🚀
""")

    # Connect to Gmail SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
    print(f"✅ Email sent to {to_email}")
