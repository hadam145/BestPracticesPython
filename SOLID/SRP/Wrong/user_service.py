# Porušení SRP – třída má více zodpovědností: uchovává data, ukládá je a posílá e-maily
class UserService:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def save(self):
        print(f"[UserService] Saving user: {self.username}")

    def send_welcome_email(self):
        print(f"[UserService] Sending welcome email to: {self.email}")
