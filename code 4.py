# Rock Paper Scissors


Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''


Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [Rock, Paper, Scissors]

import random

user_choice = int(input("Enter your choice?0 for Rock, 1 for paper or 2 for scissors\n"))
print(game_images[user_choice])

comp_choice = random.randint(0, 2)
print(f"computer choice {comp_choice}")
print(game_images[comp_choice])


if user_choice ==0:
    if comp_choice == 0:
        print("Draw")
    elif comp_choice ==1:
        print("Computer Win")
    else:
        print("You Win")
    


elif user_choice == 1:
    if comp_choice == 0:
        print("You Win")
    elif comp_choice ==1:
        print(" Draw")
    else:
        print("Computer Win")


elif user_choice == 2:
    if comp_choice == 0:
        print("Computer Win")
    elif comp_choice ==1:
        print("You Win")
    else:
        print("Draw")

else:
    print("Wrong input")

