import random

name = input("Enter your name: ")
numbers = "0123456789"
symbols = "#@$"
all = symbols+name+numbers

length = 10

password = "".join(random.sample(all, length))
print("Strong password suggested for you is:",password) 