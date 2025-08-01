# Welcome to Secure Code Game Season-1/Level-5!

# This is the last level of our first season, good luck!

import binascii
import random
import secrets
import hashlib
import os
import bcrypt

class Random_generator:

    # generates a random token
    def generate_token(self, length=8, alphabet=(
    '0123456789'
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    )):
        return ''.join(random.choice(alphabet) for _ in range(length))

    # generates salt
    def generate_salt(self, rounds=12):
        salt = ''.join(str(random.randint(0, 9)) for _ in range(21)) + '.'
        return f'$2b${rounds}${salt}'.encode()

class SHA256_hasher:

    # produces the password hash by combining password + salt because hashing
    def password_hash(self, password, salt):
        password_bytes = password.encode()
        password_hash = bcrypt.hashpw(password_bytes, salt)
        return password_hash.decode('ascii')

    # verifies that the hashed password reverses to the plain text version on verification
    def password_verification(self, password, password_hash):
        password_bytes = password.encode()
        password_hash = password_hash.encode('ascii')
        return bcrypt.checkpw(password_bytes, password_hash)

class MD5_hasher:

    # Updated to use bcrypt for secure password hashing
    def password_hash(self, password, salt=None):
        password_bytes = password.encode()
        if salt is None:
            salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password_bytes, salt)
        return password_hash.decode('ascii')

    def password_verification(self, password, password_hash):
        password_bytes = password.encode()
        password_hash = password_hash.encode('ascii')
        return bcrypt.checkpw(password_bytes, password_hash)
# a collection of sensitive secrets necessary for the software to operate
PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
SECRET_KEY = 'TjWnZr4u7x!A%D*G-KaPdSgVkXp2s5v8'
PASSWORD_HASHER = 'MD5_hasher'


# Contribute new levels to the game in 3 simple steps!
# Read our Contribution Guideline at github.com/skills/secure-code-game/blob/main/CONTRIBUTING.md