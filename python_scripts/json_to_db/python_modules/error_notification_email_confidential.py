import smtplib
import ssl
from email.message import EmailMessage
from datetime import datetime


def send_email(error_log: str = ""):
    """
    function: sent email to notify you of an ai_output error log

    @param error_log: the error log text to send it as email body
    """

    today = datetime.today()

    # Define email sender and receiver
    email_sender = "chevitarese.bruno@gmail.com"
    email_password = "twtjeqpnsbybruxx"  # if it's gmail, you will need a password app. See more in https://support.google.com/accounts/answer/185833?hl=en
    email_receiver = "bruno.chevitarese@estudante.ifes.edu.br"

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


def try_send_email(message):
    """
    Feature: make error handling to send_email function

    @param message: the message tha should be in email body
    """
    try:
        send_email(message)
    except Exception as e:
        print(e)


# Script Test
if __name__ == "__main__":
    send_email()
    print("Email successfully sent")
