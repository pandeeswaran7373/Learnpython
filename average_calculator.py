print("Average calculator for given Numbers\n")

# 🚨 Don't change the code below 👇
numbers = input("Input a list of Numbers ").split()
for n in range(0, len(numbers)):
  numbers[n] = int(numbers[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

num_total=0
for num in numbers:
    num_total += num

tot_num = 0
for total in numbers:
    tot_num += 1

average_numbers = round(num_total/tot_num)

print(average_numbers)
