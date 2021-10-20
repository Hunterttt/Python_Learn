#注意，这里的方法可能一段时间以后就不适用了，需要重新去网上搜索方法，这里用的是gmail
import smtplib
from email.mime.text import MIMEText

sender = 'tc@gmail.com'
receiver = 'ttt@hotmail.com'
pswd = 'wa5'



def send_email():
    body_of_email = 'Text to be displayed in the email'
    #msg = MIMEText(body_of_email, 'html')
    msg = MIMEText(body_of_email)
    msg['Subject'] = 'Subject line goes here'
    msg['From'] = sender
    msg['To'] = receiver

    s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
    s.login(user = sender, password = pswd)
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()

if __name__ == '__main__':
    send_email()