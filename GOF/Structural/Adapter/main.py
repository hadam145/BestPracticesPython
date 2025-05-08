from smtp_credentials import SmtpCredentials
from email_sender_adapter import EmailSenderAdapter
from email_sender import EmailSender
# Ukázka návrhového vzoru Adapter - klient pracuje s očekávaným rozhraním, adaptér překládá volání
if __name__ == "__main__":
    creds = SmtpCredentials("user@example.com", "password", "smtp.example.com", 587)
    adapter = EmailSenderAdapter(creds)
    client = EmailSender(adapter)
    client.send("john.doe@example.com", "Meeting", "Don't forget the meeting at 10 AM.")

