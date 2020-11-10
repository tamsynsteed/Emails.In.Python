import smtplib

s=smtplib.SMTP('smtp.gmail.com',587)
sender_email_id = 'tamsynsteed@gmail.com'
reciever_email_id ='adonisamber36@gmail.com'
password=input("Enter senders email password")

s.starttls()

s.login(sender_email_id,password)

message="hi guys how are you?i am doing fine"
message = message + "how was your task yesterday?"

s.sendmail(sender_email_id, reciever_email_id, message)

s.quit()
