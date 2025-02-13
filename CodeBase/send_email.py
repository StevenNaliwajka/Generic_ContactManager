import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(message, secret):
    # Create the email message
    for to_email in message.recipients_list:
        msg = MIMEMultipart()
        msg["From"] = secret.user_email_address
        msg["To"] = to_email
        msg["Subject"] = message.subject
        msg.attach(MIMEText(message.body, "plain"))

        # Send the email
        try:
            server = smtplib.SMTP(secret.smtp_server, secret.smtp_port)
            server.starttls()  # Secure the connection
            server.login(secret.user_email_address, secret.app_password)
            server.sendmail(secret.user_email_address, to_email, msg.as_string())
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print("Error:", e)