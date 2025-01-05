class User:

    def __init__(self, user_id, username, password, failed_attempts=0, is_locked=False):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.failed_attempts = failed_attempts
        self.is_locked = is_locked

    def reset_failed_attempts(self):
        self.failed_attempts = 0
        print(f"Failed attempts reset for user {self.username}.")

    def increment_failed_attempts(self):
        self.failed_attempts += 1
        print(f"Failed attempts for {self.username}: {self.failed_attempts}")

        if self.failed_attempts >= 3:
            self.lock_account()

    def lock_account(self):
        self.is_locked = True
        print(f"Account for {self.username} has been locked due to too many failed login attempts.\n")

    def validate_password(self, password):
        return self.password == password


class AuthenticationSystem:

    def __init__(self):
        self.users = {}

    def register_user(self, user_id, username, password):

        if username in self.users:
            print(f"Username {username} is already taken.")
            return

        new_user = User(user_id, username, password)
        self.users[username] = new_user
        print(f"User {username} registered successfully.\n")

    def login(self, username, password):

        user = self.users.get(username)

        if not user:
            print(f"User {username} not found.\n")
            return

        if user.is_locked:
            print(f"Account for {username} is locked. Please contact support.")
            return

        if user.validate_password(password):
            user.reset_failed_attempts()
            auth_system.update_user_status(username, user.failed_attempts, user.is_locked)
            print(f"User {username} logged in successfully.\n")
        else:
            user.increment_failed_attempts()
            auth_system.update_user_status(username, user.failed_attempts, user.is_locked)
            print(f"Incorrect password for {username}.\n")

    def update_user_status(self, username, failed_attempts, is_locked):

        user = self.users.get(username)

        if user:
            user.failed_attempts = failed_attempts
            user.is_locked = is_locked
            print(f"User {user.username}'s data updated.")


print()
auth_system = AuthenticationSystem()

auth_system.register_user(1, "neena", "password123")
auth_system.register_user(2, "helios", "mysecurepassword")

auth_system.login("neena", "password321")
auth_system.login("neena", "password111")
auth_system.login("neena", "password123")
auth_system.login("helios", "password321")
auth_system.login("helios", "mysecurepassword")
