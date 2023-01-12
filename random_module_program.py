# Import the random module here

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#find the length 

names_len= len(names)

random_select = random.randint(0,names_len-1)

who_pay= names[random_select]

print(who_pay + " is going to buy the meal today!")
