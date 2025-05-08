# Třída odpovědná pouze za odesílání e-mailu
class EmailService:
    def send_welcome_email(self, user):
        print(f"[EmailService] Sending welcome email to: {user.email}")
