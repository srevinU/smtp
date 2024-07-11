import smtplib
import email.utils
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

class Smtp:

    def __init__(self):
        load_dotenv()
        self.server = smtplib.SMTP(os.environ['SMTP_HOST'], os.environ['SMTP_PORT'])
        self.subject = os.environ['SUBJECT']
        self.to = email.utils.formataddr((os.environ['TO_NAME'],  os.environ['TO_EMAIL']))
        self.from_ = email.utils.formataddr((os.environ['FROM_NAME'],  os.environ['FROM_EMAIL']))

    def send_email(self, from_, message):
        try:
            message = MIMEText(message)
            message['To'] = self.to
            message['From'] = self.from_
            message['Subject'] = self.subject
            self.server.starttls()
            self.server.login(os.environ['SMTP_USER'], os.environ['SMTP_PASS'])
            self.server.sendmail(os.environ['TO_EMAIL'], [os.environ['TO_EMAIL']], message.as_string())
            self.server.set_debuglevel(True)
            self.server.quit()
            print(f"SUCESS: {message}")
            return {"message": "Email sent successfully."}
        except Exception as e:
            print(f"ERROR: {e}")
            return {"message": "Error sending email."}


        