#注意，这里的方法可能一段时间以后就不适用了，需要重新去网上搜索方法，这里用的是gmail
#邮件带附件
import smtplib
from email.message import EmailMessage

import mimetypes
import os,sys

os.chdir(sys.path[0]) 

message = EmailMessage()

sender = 'tc@gmail.com'
receiver = 'ttt@hotmail.com'
pswd = 'wa5'



def send_email(xflie):
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Subject line goes here'

    body_of_email = 'Text to be displayed in the email'
    message.set_content(body_of_email)



    mime_type, _ = mimetypes.guess_type(xflie)           #不懂
    mime_type, mime_subtype = mime_type.split('/')           #不懂
    with open(xflie, 'rb') as file:
        message.add_attachment(
        file.read(),
        maintype = mime_type,
        subtype = mime_subtype,
        filename = xflie)
    #print(message)


    mail_server = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
    #mail_server.set_debuglevel(1)
    mail_server.login(user = sender, password = pswd)
    mail_server.send_message(message)
    mail_server.quit()

if __name__ == '__main__':
    send_email('laal.xlsx')