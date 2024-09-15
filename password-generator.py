
import random
import string

print('--PASSWORD GENERATOR--')

characters = string.ascii_letters + string.digits + "@" + "#" + "$"+ "%"+ "&"+ "*"


amountOfPwd = input('Enter the amount of passwords you wish to generate: ')
amountOfPwd = int(amountOfPwd)

lengthOfPwd = input('Enter the desirable length of password: ')
lengthOfPwd = int(lengthOfPwd)

print('\nHere are your passwords: ')

for password in range(amountOfPwd):
   generated_passwords = ' '
   for length in range(lengthOfPwd):
     generated_passwords += random.choice(characters)
   print(generated_passwords)
