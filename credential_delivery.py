```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def deliverCredentials(credentials, email_address):
    # setup the parameters of the message
    password = "YOUR_PASSWORD"
    msg = MIMEMultipart()
    msg['From'] = "YOUR_EMAIL"
    msg['To'] = email_address
    msg['Subject'] = "Credentials Delivery"

    # add in the message body
    message = f"Dear User,\n\nHere are your credentials:\n\n{credentials}"
    msg.attach(MIMEText(message, 'plain'))

    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("Credentials successfully sent to %s:" % (msg['To']))
```