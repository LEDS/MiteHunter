import os
from dotenv import load_dotenv
import imaplib

load_dotenv()

class EmailClient:
    def __init__(self, imap_url):
        self.email_user = os.getenv("EMAIL_USER")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.imap_url = imap_url
        self.mail = None

    def connect(self):
        self.mail = imaplib.IMAP4_SSL(self.imap_url)
        self.mail.login(self.email_user, self.email_password)

    def select_mailbox(self, mailbox='inbox'):
        if not self.mail:
            self.connect()
        self.mail.select(mailbox)

    def search_emails(self, criteria):
        if not self.mail:
            self.connect()
        result, data = self.mail.search(None, criteria)
        return data[0].split()

    def mark_as_read(self, email_id):
        if not self.mail:
            self.connect()
        self.mail.store(email_id, '+FLAGS', '(\\Seen)')

    def mark_as_deleted(self, email_id):
        if not self.mail:
            self.connect()
        self.mail.store(email_id, '+FLAGS', '(\\Deleted)')

    def fetch_flags(self, email_id):
        if not self.mail:
            self.connect()
        _, status = self.mail.fetch(email_id, '(FLAGS)')
        return status[0].split()

    def fetch_header(self, email_id):
        if not self.mail:
            self.connect()
        result, message_data = self.mail.fetch(email_id, '(BODY[HEADER.FIELDS (FROM DATE)])')
        return message_data[0][1]

    def fetch_email_body(self, email_id):
        if not self.mail:
            self.connect()
        result, data = self.mail.fetch(email_id, '(RFC822)')
        return data[0][1]

    def close_connection(self):
        if self.mail:
            self.mail.logout()
            self.mail = None