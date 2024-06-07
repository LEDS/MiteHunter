from datetime import datetime
import base64
import email
import os

def decode_utf8(s: str) -> str:
    string = base64.b64decode(s[10:])
    return string.decode('utf-8')

class EmailProcessor:
    def __init__(self, email_client):
        self.email_client = email_client

    def process_email(self, email_id):
        flags = self.email_client.fetch_flags(email_id)
        if b'(\\Seen))' in flags:
            self.email_client.mark_as_deleted(email_id)
        else:
            self.email_client.mark_as_read(email_id)

            header = self.email_client.fetch_header(email_id)
            sender_email = email.message_from_bytes(header).get("From")
            email_date = email.message_from_bytes(header).get("Date")

            formatted_date = datetime.strptime(email_date, "%a, %d %b %Y %H:%M:%S %z").strftime("%Y%m%d")

            email_body = self.email_client.fetch_email_body(email_id)
            msg = email.message_from_bytes(email_body)
            email_text = self.fetch_email_text(msg)
            text = " ".join(email_text.split())

            folder_name = f"{sender_email.split('<')[-1].split('>')[0]}_{text}_{formatted_date}"
            full_path = os.path.join('images_input', folder_name)

            if not os.path.exists(full_path):
                os.makedirs(full_path)

            for part in msg.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue

                filename = part.get_filename()
                if filename:
                    if filename.startswith('=?UTF-8?B?'):
                        filename = decode_utf8(filename)

                    filepath = os.path.join(full_path, filename)
                    open(filepath, 'wb').write(part.get_payload(decode=True))

    def fetch_email_text(self, msg):
        email_text = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    email_text = part.get_payload(decode=True).decode("utf-8")
                    break
        else:
            email_text = msg.get_payload(decode=True).decode("utf-8")

        return email_text