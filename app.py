from flask import Flask, render_template, request, redirect, session
import threading
import time
import schedule
import os
from dotenv import load_dotenv
from tasks import add_task, check_tasks

# Load environment
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# ---------------- LOGIN PAGE ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        session["email"] = email
        return redirect("/dashboard")
    return render_template("login.html")

# ---------------- DASHBOARD ----------------
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "email" not in session:
        return redirect("/")

    if request.method == "POST":
        task = request.form["task"]
        date = request.form["date"]
        time_input = request.form["time"]

        remind_time = f"{date} {time_input}"
        user_email = session["email"]

        add_task(task, remind_time, user_email)
        return "✅ Reminder set successfully!"

    return render_template("dashboard.html")

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ---------------- BACKGROUND SCHEDULER ----------------
def run_scheduler():
    schedule.every(1).minutes.do(check_tasks)
    while True:
        schedule.run_pending()
        time.sleep(1)

scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.daemon = True
scheduler_thread.start()

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)
