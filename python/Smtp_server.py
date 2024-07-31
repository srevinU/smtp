import smtplib
import email.utils
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

class Smtp:

    def __init__(self):
        load_dotenv()
        self.server = smtplib.SMTP(os.environ['SMTP_HOST'], 587)
        self.to = email.utils.formataddr((os.environ['TO_NAME'],  os.environ['TO_EMAIL']))

    def send_email(self, from_, message, instance):
        try:
            message = MIMEText(message)
            message['To'] = self.to
            message['From'] = from_
            message['Subject'] = f"[Portfolio][{instance}] Contact message:"
            self.server.starttls()
            self.server.login(os.environ['SMTP_USER'], os.environ['SMTP_PASS'])
            self.server.sendmail(os.environ['TO_EMAIL'], [os.environ['TO_EMAIL']], message.as_string())
            self.server.set_debuglevel(True)
            self.server.quit()
            print(f"SUCESS: {message}")
            return {"status": 200, "message": "Email sent successfully."}
        except Exception as e:
            print(f"ERROR: {e}")
            return {"status": 500, "message": "Error sending email."}


        