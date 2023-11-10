# Feature:
# This module is responsible for storing the function tha send an email alert to specifc email

# External modules
import smtplib
import ssl
from email.message import EmailMessage
from datetime import datetime


def send_email(error_log: str = ""):
    """
    function:
        send an email to notify you of a ai_output error log

    param:
        error_log (str) -> get an error log to send it as the body of the email

    return:
        None
    """

    today = datetime.today()

    # Define email sender and receiver
    email_sender = "your_email_here"
    email_password = "password"  # if it's gmail, you will need a password app. See more in https://support.google.com/accounts/answer/185833?hl=en
    email_receiver = "email that will recive the alert"

    # Set the subject and body of the email
    subject = 'ErrorLog'
    body = f"""
Alert! A ai_output error log was added on {today.day}/{today.month}/{today.year} at {today.hour}:{today.min};

{error_log}
"""

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


# Script Test
if __name__ == "__main__":
    send_email()
    print("Email successfully sent")
