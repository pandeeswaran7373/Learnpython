print("remaining live count in life")
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#change str to int

age_as_int=(int(age))

#how many years we live in earth

years=(90-age_as_int)

#calculate age into days,weeks months
days= (365*years)
weeks = (years*52)
months = (years*12)

messge=(f"You have {years} years, You have {days} days, {weeks} weeks, and {months} months left.")

print(messge)
