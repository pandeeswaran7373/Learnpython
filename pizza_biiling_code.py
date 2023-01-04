# 🚨 Don't change the code below 👇
print("Pizza Billing App\n")

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

# find which size Pizza cutomer want

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

# ask customer to add pepperoni in pizza

if add_pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill +=3

# ask customer to add extra cheese in pizza

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
