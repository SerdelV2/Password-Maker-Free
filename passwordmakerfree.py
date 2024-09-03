import random
import string
import os
import pyperclip
from config import *

if not os.path.exists(f'{path}'):
    os.makedirs(f'{path}')

origin = input("What is this password for? ")
file = open(f'{path}Password_for_{origin}.txt', "w")
file.write(f'This file contains your password for {origin}.')

password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(passwordlen))
pyperclip.copy(f'{password}')
print(f'Your password has been created and it has been copied to clipboard! \nHere it is -->  {password}')
file.write(f'\nPassword:{password}')
loginOption = input("Do you want to add to file additional login or e-mail? [Y/n]")
if loginOption == 'Y':
    login = input("Type your login or e-mail here:")
    file.write(f'\nLogin:{login}')
file.close()
print('Your file has been successfully saved!')
