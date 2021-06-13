# Email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from pathlib import Path

message = MIMEMultipart()
message["from"] = "ronnapon.pra@gmail.com"
message["to"] = "ronnapon.pra@gmail.com"
message["subject"] = "Hello Ronnpon"
message.attach(MIMEText("Body"))
#message.attach(MIMEImage(Path("Big.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("ronnapon.pra@gmail.com", "XXX")
    smtp.send_message(message)
    print("Sent..")
