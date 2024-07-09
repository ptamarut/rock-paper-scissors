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

#Write your code below this line 👇
import random

game_images = [rock, paper, scissors]
computer_score = 0
user_score = 0

while True:
    izbor = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    if izbor >= 3 or izbor < 0:
        print("You can't choose this number. You lose!")
        break
    else :
        print(game_images[izbor])
        computer_choice = random.randint(0, 2)
        print("Computer choose:")
        print(game_images[computer_choice])

        if izbor == 0 and computer_choice == 2:
            print("You win!")
            user_score += 1
        elif izbor == 1 and computer_choice == 0:
            print("You win!")
            user_score += 1
        elif izbor == 2 and computer_choice == 1:
            print("You win!")
            user_score += 1
        elif izbor == computer_choice:
            print("It's a draw!")
        else :
            print("You lose!")
            computer_score += 1

    print(f"Your score {user_score} : {computer_score} Computer score")
    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()

    if (play_again == 'n') :
        break
    elif (play_again != 'n' or play_again != 'y') :
        input("Do you want to play again? Type 'y' or 'n': ").lower()


