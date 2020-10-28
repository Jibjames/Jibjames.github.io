"""
Mastermind Game
Author: James Bridges
CS 160
10/21/20

"""

def welcome():
    print("Welcome to MASTERMIND!")

#generates code.  Ran once at beginning
def generate_cpu_code():
    import random

    colors = "RBGP"
    cpu_code = []

    for i in range(4):
        cpu_code.append(random.choice(colors))

    return cpu_code

#gets player input and error checks
def get_player_code():
    print("Make your guess!")
    print("'R'ed, 'B'lue, 'G'reen, or 'P'urple")

    while True:
        player_code = input(">>>").upper()
        player_code = list(player_code)

        valid_count = 0
        for item in player_code:
            if item in ["R", "B", "G", "P"]:
                valid_count += 1

        if valid_count == 4:
            break
        else:
            print("INVALID INPUT")

    return player_code

#returns array of white/blacks?  Then if all black you win!
def check_guess(cpu_code, player_code):
    pegs = []

    def clone_it(cpu_code):
        code_clone = cpu_code[:]
        return code_clone

    cpu_code_clone = clone_it(cpu_code)

    for j in range(4):
        if player_code[j] == cpu_code_clone[j]:
            cpu_code_clone[j] = "X"
            pegs.insert(0, "B")

    print("TESTING ONLY! cpu:", cpu_code)

    for j in range(4):
        if player_code[j] in cpu_code_clone:
            pegs.append("W")
            cpu_code_clone.remove(player_code[j])

    return pegs

#displays the complete board, with all guesses, and pegs
def display_board(guess_l, peg_l):
    print("Board:")
    for i in range(len(guess_l)):
        print(guess_l[i], "pegs: ", peg_l[i])

#promps user to play again, returns 'Y' or 'N'
def play_again():
    print("Play Again? 'Y'es, 'N'o")
    while True:
        choice = input(">>>").upper()
        if choice == "Y":
            return "Y"
        elif choice == "N":
            return "N"
        else:
            print("INVALID INPUT")

def main():
    welcome()
    while True:
        cpu_code = generate_cpu_code()
        #print(cpu_code)
        round = 1
        guess_board = []
        peg_board = []

        while round <= 10:
            print("")
            print("ROUND", round)

            player_code = get_player_code()
            guess_board.append(player_code)            

            guess_array = check_guess(cpu_code, player_code)
            peg_board.append(guess_array)
            display_board(guess_board, peg_board)

            if guess_array == ["B", "B", "B", "B"]:
                print("***********")
                print("YOU WIN!!!!")
                print("***********")
                break

            elif round == 10:
                print("************")
                print("YOU LOSE!!!!")
                print("************")

            round += 1
            
        if play_again() == "N":
            break

main()




