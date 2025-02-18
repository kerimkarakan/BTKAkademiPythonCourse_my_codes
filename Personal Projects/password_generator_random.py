from string import *
from random import *

plenght = randint(10,30)

print('''Character sets:
         1. Digits
         2. Letters
         3. Special characters
         4. Finish''')

character_list = ""

while True:
    number = int(input("Choose a character set for your password: "))

    if number == 1:
        character_list += digits
    elif number == 2:
        character_list += ascii_letters
    elif number == 3:
        character_list += punctuation
    elif number == 4:
        break
    else:
        print("You entered an invalid character set!")

generated_password = []

for i in range(plenght):
    randomc = choice(character_list)
    generated_password.append(randomc)


print("Here is your randomly generated password: " + "".join(generated_password))