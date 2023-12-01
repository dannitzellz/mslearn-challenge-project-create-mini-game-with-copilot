#create a rock paper scissors game
#user will input their choice
#computer will randomly select a choice
#compare the choices and decide who wins
#display the results
import random
import os
import time

#create a variable to store the user's score
user_score = 0
def play():
    print("Welcome to Rock, Paper, Scissors!")
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()
    if user == 'r' or user == 'p' or user == 's':
        pass
    else:
        print("Invalid input. Please try again.")
        play()
    time.sleep(1)
    print("Rock...")
    time.sleep(1)
    print("Paper...")
    time.sleep(1)
    print("Scissors...")
    time.sleep(1)
    print("Shoot!")
    time.sleep(1)
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        print("It's a tie!")
    elif is_win(user, computer):
        #increase the user's score by 1
        global user_score
        user_score += 1
        print("You won!")
    else:
        print("You lost!")
    time.sleep(1)
    play_again = input("Would you like to play again? (y/n)")
    if play_again == 'y':
        os.system('clear')
        play()
    else:
        #show the user their final score
        print(f"Your final score is {user_score}")
        print("Thanks for playing!")
        time.sleep(10)
        os.system('clear')
        exit()
    
    #create function to determine if user won
def is_win(player, opponent):
    #return true if player wins
    #r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False

#create main function
if __name__ == '__main__':
    play()
