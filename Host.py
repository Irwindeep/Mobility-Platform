import random

menu="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV!@#$%^&*()123456789"

password=""
for x in range(0,7):
    password_menu=random.choice(menu)
    password=password+password_menu

print("Your password is: ",password)
print("Do not share this password with anyone.")
