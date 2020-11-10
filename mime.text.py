import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email_id = "tamsynsteed@gmail.com"
reciever_email_id ="adonisamber36@gmail.com"
password =input("enter password")

subject ="greetings"
msg=MIMEMultipart()
msg['From'] =sender_email_id
msg['To']=reciever_email_id
msg['Subject']=subject
body="hi guys whatsup\n"
body= body+"yo biatch"

msg.attach(MIMEText(body,'plain'))
text=msg.as_string()

s =smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(sender_email_id,password)

s.sendmail(sender_email_id, reciever_email_id,text)

s.quit()
