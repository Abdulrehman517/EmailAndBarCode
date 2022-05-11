from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
from string import Template
template = Template(Path('Template.html').read_text())
message = MIMEMultipart()
message['from'] = 'Abdulrehman'
message['to'] = 'abdulrehman67846@gmail.com'
message['subject'] = 'this is test email'
body = template.substitute({'name': 'Junaid Khan'})
message.attach(MIMEText(body, 'html'))
message.attach(MIMEImage(Path('e.PNG').read_bytes()))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your email', 'your password')
    smtp.send_message(message)
    print('sent...')