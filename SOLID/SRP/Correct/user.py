# Každá třída má pouze jednu odpovědnost (SRP)
class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
