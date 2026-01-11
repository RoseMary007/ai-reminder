from datetime import datetime
from email_sender import send_email

tasks = []

def add_task(task, remind_time, email):
    tasks.append({
        "task": task,
        "time": remind_time,
        "email": email
    })
    print("✅ Task added:", task, remind_time, email)

def check_tasks():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    for task in tasks[:]:
        if task["time"] == now:
            send_email(task["email"], task["task"], task["time"])
            tasks.remove(task)
