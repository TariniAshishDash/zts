import pyotp
import os

class MFAHandler:
    def __init__(self, user_id):
        self.user_id = user_id
        self.totp = pyotp.TOTP(self._generate_secret())
        self.backup_codes = self._generate_backup_codes()

    def _generate_secret(self):
        # Generate a new secret key for TOTP
        return pyotp.random_base32()

    def _generate_backup_codes(self, count=10):
        # Generate a list of unique backup codes
        return [os.urandom(4).hex() for _ in range(count)]

    def get_totp(self):
        # Return the current TOTP token
        return self.totp.now()

    def verify_totp(self, token):
        # Verify the provided TOTP token
        return self.totp.verify(token)

    def use_backup_code(self, code):
        # Validate and use a backup code
        if code in self.backup_codes:
            self.backup_codes.remove(code)
            return True
        return False

# Example usage:
# mfa = MFAHandler(user_id='user@example.com')
# print(mfa.get_totp())
# print(mfa.verify_totp(input('Enter TOTP: ')))
# print(mfa.use_backup_code(input('Enter backup code: ')))
