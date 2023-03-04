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

print("Welcome to the Rock Paper Scissors simulation!")
choose = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors. \n"))


if choose > 2 or choose < 0:
  print("You typed an invalid number, you lose") 
else: 
  elements = [rock, paper, scissors]
  
  your_choice = elements[choose]
  
  print(f"You chose: {your_choice}")
  
  computer_choice = elements[random.randint(0,2)]
  
  print(f"Computer chose: {computer_choice}")
  
  if(choose == 2):
    if(computer_choice == elements[0]):
      print("You lose")
    else:
      print("You win")
  
  if(choose == 1):
    if(computer_choice == elements[2]):
      print("You lose")
    else:
      print("You win")
  
  if(choose == 0):
    if(computer_choice == elements[1]):
      print("You lose")
    else:
      print("You win")
  
  if(your_choice == computer_choice):
    print("Draw")