```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def deliver_credentials(email_address, credentials):
    # setup the parameters of the message
    password = "YOUR_PASSWORD"
    msg = MIMEMultipart()
    msg['From'] = "YOUR_EMAIL"
    msg['To'] = email_address
    msg['Subject'] = "Credentials Delivery"

    # add in the message body
    message = f"Dear Owner-Operator,\n\nHere are your login credentials:\n\n{credentials}\n\nBest,\nAGI"
    msg.attach(MIMEText(message, 'plain'))

    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("Successfully sent email to %s:" % (msg['To']))
```