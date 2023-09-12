```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def deliverCredentials(email_address, credentials):
    # setup the parameters of the message
    password = "YOUR_PASSWORD"
    msg = MIMEMultipart()

    msg['From'] = "YOUR_EMAIL"
    msg['To'] = email_address
    msg['Subject'] = "Credentials Delivery"

    # add in the message body
    msg.attach(MIMEText('Find attached the credentials.', 'plain'))

    # load credentials in a file
    filename = 'credentials.txt'
    with open(filename, 'w') as f:
        f.write(credentials)

    # setup the attachment
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # add attachment to message
    msg.attach(part)

    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("Credentials successfully sent to %s:" % (msg['To']))

# Test the function
deliverCredentials("test@example.com", credentials)
```