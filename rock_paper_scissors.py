# ascii art for when player throws a choice

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

user_choice = input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. \n')

computer_choice = random.randint(0, 2)

print(f'Computer chose {computer_choice}')