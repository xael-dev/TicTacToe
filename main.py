from IPython.display import clear_output

player_turn = 1

#Board state maintenance, uses a passed in dictionary to update positions on the board
def board_state(matrix_positions = ['.','.','.','.','.','.','.','.','.']): #TODO: Clean this up later, make this list the universal default
    # matrix_positions = ["a","b","c","d","e","f","g","h","i"] Debug purposes :P
    print(matrix_positions[0],matrix_positions[1],matrix_positions[2])
    print(matrix_positions[3], matrix_positions[4], matrix_positions[5])
    print(matrix_positions[6], matrix_positions[7], matrix_positions[8])

#Define game status whether the player wants to play or not
def game_start():
    confirm = input("Welcome to TicTacToe, would you like to play? (yes/no): ")

    if confirm == "y" or confirm == "yes":
        player_name1 = str(input("What is your name player 1: "))
        player_name2 = str(input("What is your name player 2: "))
        clear_output()
        board_state()
        player_choice(player_name1, player_name2)
    elif confirm == "n" or confirm == "no":
        print("Maybe next time!")
    else:
        print("Sorry, that input isn't valid")

#Define user input
def player_choice(player_name1, player_name2):
    matrix_positions = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    global player_turn
    move_count = 0

    while player_turn != None and move_count <= 9:
        if player_turn == 1:
            clear_output()
            move_count += 1
            position_choice = str(input(player_name1 + " choose a position number (1-9): "))

            if matrix_positions[int(position_choice)-1] == "X" or matrix_positions[int(position_choice)-1] == "O":
                player_turn = 1
                continue

            if position_choice.isdigit() and (int(position_choice)-1) in range(0,9):
                player_symbol = "X"
                matrix_positions[int(position_choice)-1] = player_symbol
                board_state(matrix_positions)
                game_logic(matrix_positions, player_name1,player_symbol)

                if player_turn == 3:
                    break
                else:
                    player_turn = 2
            else:
                    print("The number you entered was invalid")
            

        if player_turn == 2:
            clear_output()
            position_choice = str(input(player_name2 + " choose a position number (1-9): "))

            if matrix_positions[int(position_choice)-1] == "X" or matrix_positions[int(position_choice)-1] == "O":
                player_turn = 2
                continue

            if position_choice.isdigit() and (int(position_choice)-1) in range(0,9):
                player_symbol = "O"
                matrix_positions[int(position_choice)-1] = player_symbol
                board_state(matrix_positions)
                game_logic(matrix_positions, player_name2, player_symbol)
                
                if player_turn == 3:
                    break
                else:
                    player_turn = 1
            else:
                print("The number you entered is invalid")

#Game logic
def game_logic(matrix_positions, player_name, player_symbol):
    global player_turn

    #Horizontal conditions
    if player_symbol in matrix_positions[0] and player_symbol in matrix_positions[1] and player_symbol in matrix_positions[2]:
        player_turn = 3
        print(f"{player_name} has won!")
    elif player_symbol in matrix_positions[3] and player_symbol in matrix_positions[4] and player_symbol in matrix_positions[5]:
        player_turn = 3
        print(f"{player_name} has won!")
    elif player_symbol in matrix_positions[6] and player_symbol in matrix_positions[7] and player_symbol in matrix_positions[8]:
        player_turn = 3
        print(f"{player_name} has won!")

    #Vertical conditions
    elif player_symbol in matrix_positions[0] and player_symbol in matrix_positions[3] and player_symbol in matrix_positions[6]:
        player_turn = 3
        print(f"{player_name} has won!")
    elif player_symbol in matrix_positions[1] and player_symbol in matrix_positions[4] and player_symbol in matrix_positions[7]:
        player_turn = 3
        print(f"{player_name} has won!")
    elif player_symbol in matrix_positions[2] and player_symbol in matrix_positions[5] and player_symbol in matrix_positions[8]:
        player_turn = 3
        print(f"{player_name} has won!")

    #Diagonal conditions
    elif player_symbol in matrix_positions[0] and player_symbol in matrix_positions[4] and player_symbol in matrix_positions[8]:
        player_turn = 3
        print(f"{player_name} has won!")
    elif player_symbol in matrix_positions[2] and player_symbol in matrix_positions[4] and player_symbol in matrix_positions[6]:
        player_turn = 3
        print(f"{player_name} has won!")
    else:
        return


#Game Programming
game_start()