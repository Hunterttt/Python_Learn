import smtplib
from email.mime.text import MIMEText

sender = 'tc@gmail.com'
receiver = 'ttt@hotmail.com'
body_of_email = 'Text to be displayed in the email'

#msg = MIMEText(body_of_email, 'html')
msg = MIMEText(body_of_email)
msg['Subject'] = 'Subject line goes here'
msg['From'] = sender
msg['To'] = receiver

def send_email():
    s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
    s.login(user = 'tc@gmail.com', password = 'wa5')
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()

if __name__ == '__main__':
    send_email()