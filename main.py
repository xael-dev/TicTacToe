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

    #TODO: Validate and convert these inputs to appropriate array mappings in matrix_positions list
    #TODO: Validate if names are present and if not assign default to them
    while player_turn == 1:
        clear_output()
        position_choice = int(input(player_name1 + " choose a position number (1-9): "))
        matrix_positions[position_choice] = "X"
        board_state(matrix_positions)
        game_logic(matrix_positions, player_turn)
        player_turn = 2

        if player_turn == 2:
            clear_output()
            position_choice = int(input(player_name2 + " choose a position number (1-9): "))
            matrix_positions[position_choice] = "O"
            board_state(matrix_positions)
            game_logic(matrix_positions, player_turn)
            player_turn = 1
        
        if player_turn == 3:
            print("player has won!") #Break the loop here and declare appropriate winner
            break
        
#Game logic
def game_logic(matrix_positions, player_turn):
    win_state = None #print(f"Player {player_turn} has won!")

    if "X" in matrix_positions[0] and "X" in matrix_positions[1] and "X" in matrix_positions[2]:
        print("win") #debug
        player_turn = 3
    return player_turn, matrix_positions, win_state




#Game Programming
game_start()