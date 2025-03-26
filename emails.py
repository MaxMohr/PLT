import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_mail(name_one: str, name_two: str, mail: str, percentage: int):
    sender_email = os.getenv("EMAIL")
    receiver_email = mail
    password = os.getenv("PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    subject = "Dein Test-Ergebnis"
    body = (f"Dein Testergebnis ist da:\n"
            f"{name_one} liebt {name_two} zu {percentage}%.\n\n"
            f"Vielen Dank fürs Nutzen des Panda Love Tests!")

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, 587) as server:
            server.starttls()  # Verschlüsselung aktivieren
            server.login(sender_email, password)  # Einloggen
            server.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(f"Fehler: {e}")