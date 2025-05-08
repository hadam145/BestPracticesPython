# Ukázka porušení SRP – vše v jedné třídě
from user_service import UserService

if __name__ == "__main__":
    user = UserService("jdoe", "jdoe@example.com")
    user.save()
    user.send_welcome_email()
