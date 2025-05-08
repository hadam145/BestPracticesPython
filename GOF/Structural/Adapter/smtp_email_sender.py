from GOF.Structural.Adapter.smtp_credentials import SmtpCredentials
# Třída, která umí odesílat e-maily přes SMTP (má jiné rozhraní než očekává klient)
class SmtpEmailSender:
    def __init__(self, credentials: SmtpCredentials):
        self.credentials = credentials

    def send_smtp_email(self, to_address: str, subject: str, body: str):
        print(f"[SMTP] Sending email to {to_address} via {self.credentials.server}:{self.credentials.port}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
