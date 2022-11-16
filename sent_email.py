from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
 
def sent_for_email(text):
    msg = MIMEMultipart()
    
    password = "cZ4kK3Vshm7qevciudHh"
    msg['From'] = "riga03@internet.ru"
    msg['To'] = "ferkur800@gmail.com"
    msg['Subject'] = f'Позвонить!'

    msg.attach(MIMEText(text))

    server = smtplib.SMTP('smtp.mail.ru: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.send_message(msg)
    server.quit()


