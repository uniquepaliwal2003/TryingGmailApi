import imaplib
import time
from email import message_from_bytes
from email.header import decode_header

# Your Gmail credentials
email_address = "b210475@skit.ac.in"
password = "86625549"

# Connect to Gmail IMAP server
mail = imaplib.IMAP4_SSL("imap.gmail.com")

# Login to your Gmail account
mail.login(email_address, password)

# Select the mailbox you want to check (e.g., "inbox")
mail.select("inbox")

def check_emails():
    # Search for all unseen emails
    status, messages = mail.search(None, "(UNSEEN)")

    if status == "OK":
        for num in messages[0].split():
            # Fetch the email by its sequence number
            status, msg_data = mail.fetch(num, "(RFC822)")
            
            if status == "OK":
                # Parse the email content
                msg = message_from_bytes(msg_data[0][1])
                subject, encoding = decode_header(msg["Subject"])[0]
                
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or "utf-8")
                
                print(f"New Email - Subject: {subject}")

# Run the program indefinitely
while True:
    check_emails()
    
    # Sleep for 15 minutes before checking again
    time.sleep(15 * 60)

# Close the connection
mail.logout()
