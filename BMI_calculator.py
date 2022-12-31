#BMI Calculator

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# BMI Formula 
#BMI=weight(kg)/height*height(meter)

BMI = int(weight)/float(height)**2
print(int(BMI))

print("what are your results based on BMI see below\n")

print(str("""Underweight (Severe thinness)< 16.0\n
Underweight (Moderate thinness)	16.0 – 16.9\n
Underweight (Mild thinness)	17.0 – 18.4\n
Normal range	18.5 – 24.9	 \n
Overweight (Pre-obese)	25.0 – 29.9\n
Obese (Class I)	30.0 – 34.9\n
Obese (Class II)	35.0 – 39.9\n
Obese (Class III)	≥ 40.0  \n"""))
