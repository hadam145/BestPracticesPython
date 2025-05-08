# Třída reprezentující SMTP přihlašovací údaje
class SmtpCredentials:
    def __init__(self, username: str, password: str, server: str, port: int):
        self.username = username
        self.password = password
        self.server = server
        self.port = port
