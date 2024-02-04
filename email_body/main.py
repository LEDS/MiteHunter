from modules.email_client import EmailClient
from modules.email_processor import EmailProcessor
from dotenv import load_dotenv
import schedule
import time

load_dotenv()

def check_emails(email_client, email_processor):
    try:
        email_client.select_mailbox('inbox')  # Ensure mailbox is selected
        criteria = '(SUBJECT "Amostra de morango")'
        email_ids = email_client.search_emails(criteria)

        for email_id in email_ids:
            email_processor.process_email(email_id)

    finally:
        email_client.close_connection()

def main():
    imap_url = 'imap.gmail.com'
    email_client = EmailClient(imap_url)
    email_processor = EmailProcessor(email_client)

    schedule.every(1).seconds.do(check_emails, email_client, email_processor)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()