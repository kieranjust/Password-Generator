import random
import string

password_characters = random.sample(string.ascii_letters, k=10)
password = ''.join(password_characters)
print(password)
