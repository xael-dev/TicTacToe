from IPython.display import clear_output

#Board state maintenance, uses a passed in dictionary to update positions on the board
def board_state(matrix_positions = ['.','.','.','.','.','.','.','.','.']): #TODO: Clean this up later, make this list the universal default
    # matrix_positions = ["a","b","c","d","e","f","g","h","i"] Debug purposes :P
    print(matrix_positions[0],matrix_positions[1],matrix_positions[2])
    print(matrix_positions[3], matrix_positions[4], matrix_positions[5])
    print(matrix_positions[6], matrix_positions[7], matrix_positions[8])

#Define game status whether the player wants to play or not
def game_state(confirm):
    confirm = input("Welcome to TicTacToe, would you like to play? (yes/no): ")
    player_name1 = str(input("What is your name player 1: "))
    player_name2 = str(input("What is your name player 2: "))
    
    display_game = board_state()

    if confirm == "y" or confirm == "yes":
        player_choice(player_name1, player_name2)
    elif confirm == 'r': #r should only be set by another method, may restructure or rename in the future
        clear_output()
        board_state()
    else: 
        print("Sorry, that input isn't valid")

#Define user input
def player_choice(player_name1, player_name2 = "Deonda"):
    matrix_positions = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    player_turn = 1

    #The following is just a placeholder, make these into a function to avoid repetition, testing logical flow here
    while player_turn == 1:
        position_choice = int(input(f"{player_name1} choose a position number (1-9): "))
        matrix_positions.insert(position_choice, "X")
        player_turn = 2

    while player_turn == 2:
        position_choice = int(input(f"{player_name2} choose a position number (1-9): "))
        matrix_positions.insert(position_choice, "O")
        player_turn = 1
        
    

#Game logic
def game_logic():
    pass


#Game Programming
board_state()