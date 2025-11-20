import random

choices = ["Rock", "Paper", "Scissor"]

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor:\n")

# Validate input
if user_choice not in ['0', '1', '2']:
    print("Invalid input! Please enter 0, 1, or 2.")
    exit()

user_choice = int(user_choice)
computer_choice = random.randint(0, 2)

print(f"You choose {choices[user_choice]}")
print(f"Computer chooses {choices[computer_choice]}")

if user_choice == computer_choice:
    print("Result is a draw")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("Congrats, you win !!!")
else:
    print("Oops, you lose")
