import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
def send_email(email, receiver_email, message):
    try:
        subject="Your Health Recommendations from Blood Test Results"
        text = f"Subject: {subject}\n\n{message}"
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, os.getenv('MODEL_URL'))
        server.sendmail(email, receiver_email, text)
        server.quit()
        print("Email has been sent to " + receiver_email)
    except Exception as e:
        print("Failed to send email. Error:", e)
