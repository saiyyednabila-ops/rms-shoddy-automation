import win32com.client
from datetime import datetime

class EmailHandler:
    def __init__(self):
        self.outlook = win32com.client.Dispatch("Outlook.Application")
        self.namespace = self.outlook.GetNamespace("MAPI")

    def login(self, email_address):
        # Login functionality (handled by Outlook's default behavior)
        pass

    def scan_sent_box(self):
        sent_items = self.namespace.GetDefaultFolder(5)  # 5 refers to the Sent Items folder
        return sent_items.Items

    def filter_emails(self, start_date, urgent=False):
        sent_items = self.scan_sent_box()
        filtered_emails = []
        for item in sent_items:
            if item.SentOn >= start_date and (urgent == item.Importance == 2):  # Urgent = 2
                filtered_emails.append(item)
        return filtered_emails

    def check_email_threads(self, email):
        # Function to check if email threads are completed
        # Dummy logic for completion check
        return email.Unread == False

    def extract_rms_ids(self, email):
        # Extract RMS IDs from the subject line
        subject = email.Subject
        rms_ids = [word for word in subject.split() if word.startswith("RMS-")]
        return rms_ids

# Example usage
if __name__ == "__main__":
    email_handler = EmailHandler()
    email_handler.login("your_email@domain.com")