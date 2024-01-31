print(
    " ***************** Tic Tac Toe ******************\n*===============================================*\n||                  3x3  Box                   ||\n||   -----------   -----------  -----------    ||\n||        |             |            |         ||\n||        |             |            |         ||\n||        |             |            |         ||\n||                                             ||\n||             \   /            _____          ||\n||              \ /      or    |     |         ||\n||              / \            |     |         ||\n||             /   \            -----          ||\n*===============================================*")
# introduction to game and instruction
print("Hi user ,\n"
      "here we play a game tic-tac-toe to remember the childhood :\n"
      "so here are the instruction : \n"
      "1. Here we use [ ANY TYPE OF SYMBOL including emoji also ] for input \n"
      "2. If there is a straight or horizontal cut of X or O are winners \n"
      "3. There is only 3x3 box \n"
      "4. If you want to \'QUIT\' type \"0000\" \n")
# getting the input from the user
t3board = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal wins
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical wins
                        (0, 4, 8), (2, 4, 6)]


# function for tic-tac-toe boxes:
def singlelines():
    print("       |          |        ")


def lines():
    print("       |          |        ")
    print("---------------------------")
    print("       |          |        ")


def boxes(b):
    singlelines()
    print("  ", b[0], "  |   ", b[1], "    |   ", b[2], " ")
    lines()
    print("  ", b[3], "  |   ", b[4], "    |   ", b[5], " ")
    lines()
    print("  ", b[6], "  |   ", b[7], "    |   ", b[8], " ")
    singlelines()
    check_for_potential_winner(b)
    # if check_for_potential_winner(b):
    #     print("Match Draws !")


def check_for_potential_winner(b):
    for listing in winning_combinations:
        if b[listing[0]] == b[listing[1]] == b[listing[2]] != "a":
            print(f"Congrats!, Player {b[listing[0]]} wins the game.")
    # if "a" not in b:return
    # print("Match Draws! ")
    # return False  # return True
    # for listing in winning_combinations:
    #     if b[listing[0]] not in b:  # Check if all positions are filled and no one has won
    #         print("Match Draw!")


# replacing the character :
def changing_function(t, entered1, entered2, uin1, uin2):
    new_board = t
    for i in range(len(new_board)):
        new_board[i] = new_board[i].replace(entered1, uin1)
        new_board[i] = new_board[i].replace(entered2, uin2)
    boxes(new_board)
    # for listing in winning_combinations:
    #     if new_board[listing[0]] == new_board[listing[1]] == new_board[listing[2]] != "a":
    #         print(f"Congrats!, Player {new_board[listing[0]]} wins the game.")
    # else  not in new_board:
    #         print("Match draws")


def StartingPoint():
    print("Enter player 1 selected SYMBOL :")
    userinput1 = input()
    print("Enter player 2 selected SYMBOL :")
    userinput2 = input()
    summed = 1

    if userinput1 != "0000" and userinput2 != "0000":
        while userinput1 != "0000" or userinput2 != "0000":  # quit the program and concludes for visiting using "else"
            print("Round : ", summed)
            print("===================================")
            boxes(t3board)  # function for creating the
            enter1 = input("Enter the character to replace the character space [player1] : ")
            enter2 = input("Enter the character to replace the character space [player2] : ")
            if enter1 in t3board and enter2 in t3board:
                if enter1 != enter2:
                    changing_function(t3board, enter1, enter2, userinput1, userinput2)
                else:
                    print("\nBoth have entered same input ")
            elif enter1 == enter2 == "" :
                 print("\nType symbol for ")
            else:print("\nSorry! there is no variable in the box \n")
            summed += 1
    elif userinput2 == "0000" or userinput1 == "0000":
        print("\nDo you want to play again? \nThanks for visiting the Game .........!!!")
        again = input("Yes or No : ")
        if again in ['Yes', 'yes']:StartingPoint()
        else:
            print("\nThanks for visiting!!!  😊");exit()
    else:print("\nThanks for visiting!!!  😊")


StartingPoint()
print("\nDo you want to play Again ?(Y/y  or N/n) : ")
a = input()
if a == "Y" or a == "y":
    StartingPoint()
else:
    print("Thank you come again.")
