from string import *
from random import *

password_lenght = randint(10,30)

characters = ascii_letters + digits + punctuation

generated_password = ""

for i in range(password_lenght):
   generated_password += choice(characters)

print(generated_password)

