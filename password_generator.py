import string
import secrets
import random

password_length = int(input("Enter Length: "))
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
selection_list = letters + digits + special_chars

password = ''
for i in range(password_length):
    password += ''.join(secrets.choice(selection_list))

print(password)

