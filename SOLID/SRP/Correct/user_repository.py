# Třída odpovědná pouze za ukládání dat
class UserRepository:
    def save(self, user):
        print(f"[UserRepository] Saving user: {user.username}")
