import bcrypt

class PasswordManager:
    @staticmethod
    def hash_password(plain_text_password):
        # Generate a salt
        salt = bcrypt.gensalt()
        # Hash the password
        hashed_password = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    @staticmethod
    def validate_password(plain_text_password, hashed_password):
        # Validate a plain text password against a hashed password
        return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password.encode('utf-8'))

    @staticmethod
    def is_strong_password(password):
        # Implement policy check: at least 8 characters, 1 upper, 1 number, 1 special character
        if (len(password) < 8 or
            not any(char.isupper() for char in password) or
            not any(char.isdigit() for char in password) or
            not any(char in '!@#$%^&*()[]{};:,.<>?/' for char in password)):
            return False
        return True

# Example usage:
# hashed = PasswordManager.hash_password('my_secret_password')
# is_valid = PasswordManager.validate_password('my_secret_password', hashed)
# is_strong = PasswordManager.is_strong_password('MyS3cureP@ssw0rd!')