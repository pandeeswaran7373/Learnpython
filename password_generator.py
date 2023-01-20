import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

characters=['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the pypassword Genertor")

#collect user data

eng_letters = int(input("How many letters you want to create Password\n"))
num = int(input(f"How many numbers you want to create Password\n"))
symbols=int(input(f"How many symbols you want to create Password\n"))

#create password Easy way

# password =""

# for char in range(1,eng_letters+1):
#     password += random.choice(letters)

# for char in range(1,num+1):
#     password += random.choice(numbers)

# for char in range(1,symbols+1):
#     password += random.choice(characters)

# print(password)

password_list= []

for char in range (1,eng_letters+1):
    password_list += random.choice(letters)

for char in range (1,num+1):
    password_list += random.choice(numbers)

for char in range (1,symbols+1):
    password_list += random.choice(characters)

print(password_list)

random.shuffle(password_list)

print(password_list)

password = ''

for x in password_list:
    password += x 

print(f"your password is:{password}")
