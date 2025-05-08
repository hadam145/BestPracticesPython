# Ukázka správné aplikace SRP – každá třída má pouze jednu zodpovědnost
from user import User
from user_repository import UserRepository
from email_service import EmailService

if __name__ == "__main__":
    user = User("jdoe", "jdoe@example.com")
    repo = UserRepository()
    mailer = EmailService()

    repo.save(user)
    mailer.send_welcome_email(user)
