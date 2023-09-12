```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from CredentialDeliverySchema import login_credentials

def deliverCredentials():
    # Define the SMTP server credentials here
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "your-email@gmail.com"
    smtp_password = "your-password"

    # Define the email properties
    from_address = smtp_username
    to_address = login_credentials['email']
    subject = "Your Login Credentials"

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Define the email body
    body = f"Dear User,\n\nHere are your login credentials:\nUsername: {login_credentials['username']}\nPassword: {login_credentials['password']}\n\nBest,\nAGI"

    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(msg)
    server.quit()

# Call the function to deliver the credentials
deliverCredentials()
```