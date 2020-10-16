"""
Rock Paper Scissors
James Bridges
10/11/2020

"""
import random

def cpu_choice(): #Generates a random choice for the cpu
    i = random.randint(1, 3)

    if i == 1:
        return "rock"
    if i == 2:
        return "paper"
    if i == 3:
        return "scissor"

def round_result(): #Calls cpu_choice, compares with user_input, and returns the result 

    if user_input == cpu_input:
        return "tie"
    if user_input == "rock" and cpu_input == "paper":
        return "cpu"
    if user_input == "rock" and cpu_input == "scissor":
        return "user"
    if user_input == "paper" and cpu_input == "rock":
        return "user"
    if user_input == "paper" and cpu_input == "scissor":
        return "cpu"
    if user_input == "scissor" and cpu_input == "rock":
        return "cpu"
    if user_input == "scissor" and cpu_input == "paper":
        return "user"

#WELCOME
print("Welcome to Rock, Paper, Scissors!")

#Recieves number of rounds, and error checks, should be a seperate function
while True:
    print("Would you like to play 3, 5 or 7, rounds?")
    rounds = int(input(">>>")) #BREAKS IF USER ENTERS SOMETHING THAT INT CANT CONVERT LIKE 'rock'

    if rounds == 3 or rounds == 5 or rounds == 7:
        break
    else:
        print(rounds, "IS NOT A VALID # OF ROUNDS!")

round_num = 1
cpu_score = 0
user_score = 0

#Plays the game! should be a seperate function
while (round_num <= rounds):
    print("Round",round_num, "!")

    if round_num == rounds:
        print("LAST ROUND!!!")

    while True:
        user_input = input("Make your choice(rock, paper, scissor)\n>>>")

        if user_input == 'rock' or user_input == 'paper' or user_input == 'scissor':
            break
        else:
            print(user_input, "IS NOT A VALID CHOICE!")

    cpu_input = cpu_choice()
    result = round_result()
    
    print("CPU:", cpu_input)
    if result == "tie":
        print("TIE!")
    elif result == "cpu":
        print("CPU WINS THE ROUND!")
        cpu_score += 1
    elif result == "user":
        print("PLAYER WINS THE ROUND!")
        user_score += 1

    print()
    print("Score:")
    print("Player:", user_score)
    print("CPU:",cpu_score)
    print()
    round_num +=1

print("************************")

if cpu_score > user_score:
    print("CPU WINS!")
elif cpu_score < user_score:
    print("PLAYER WINS!")
else:
    print("TIE!")

print("************************")

