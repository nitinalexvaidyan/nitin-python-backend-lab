class User:
    def __init__(self):
        self.user = {}

    def add_user(self, user_name, email):
        if user_name in self.user:
            raise ValueError("User already exists")
        self.user[user_name] = email
        return True
    
    def get_user(self, user_name):
        return self.user.get(user_name)
