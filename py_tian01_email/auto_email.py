import smtplib

from email.mime.text import MIMEText

# メールを送信
def send_mail(subject, message):
	from_addr = "co.jp"
	to_addr = "hotmail.com"
	user_name = from_addr
	passwd = "wa5"
	
	msg = MIMEText(message)
	msg['Subject'] = subject
	msg['From'] = from_addr
	msg['To'] = to_addr
	
	smtp = smtplib.SMTP("smtp.mail.yahoo.co.jp", 587)
	smtp.login(user_name, passwd)
	smtp.sendmail(from_addr, to_addr, msg.as_string())
	smtp.quit()

def main():
    send_mail("連絡電話", "いつもお世話になって")

if __name__ == '__main__':
    main()
