import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_images = [rock, paper, scissors]

user_choose=int(input("what was you choose? 0 for Rock, 1 for Paper, 2 Scissors\n"))

if user_choose >= 3 or user_choose < 0:
    print("you entered Invalid Number of This game,You lose!")
else:
    print(game_images[user_choose])
    computer_choose = random.randint(0, 2)
    print("Computer choose:")
    print(game_images[computer_choose])

    if user_choose == 0 and computer_choose == 2:
        print("You win")
    elif user_choose == 2 and computer_choose == 0:
        print("You lose")
    elif user_choose > computer_choose:
        print("You win")
    elif computer_choose > user_choose:
        print("you lose")
    elif computer_choose == user_choose:
        print("Draw")
