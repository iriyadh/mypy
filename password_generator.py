import random

print ("\n\nWelcome to Riyadh's Password Generator")

chars = "!#$%&()*+,-./:;<=>?@[\]^_`'{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

number = input ('\nAmount of passwords to generate: ')
number = int(number)

length = input('\nInput your password length: ')
length = int(length)

print ('\nHere is/are your password/list of passwords: ')

for pwds in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)