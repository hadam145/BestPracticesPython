from message_sender import MessageSender
from smtp_email_sender import SmtpEmailSender
from smtp_credentials import SmtpCredentials
# Adaptér, který přizpůsobí SmtpEmailSender na rozhraní IMessageSender
class EmailSenderAdapter(MessageSender):
    def __init__(self, credentials: SmtpCredentials):
        self.smtp_sender = SmtpEmailSender(credentials)

    def send_message(self, to: str, subject: str, body: str):
        self.smtp_sender.send_smtp_email(to, subject, body)
