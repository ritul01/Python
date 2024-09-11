import random
chars="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
length=int(input("Enter length: "))
Password=""
for a in range(length):
    Password+=random.choice(chars)
print(Password)