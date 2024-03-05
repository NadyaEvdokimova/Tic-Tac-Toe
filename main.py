import os
import random

turn = 1
winning_combos = [
    [0, 1, 2],
    [0, 4, 8],
    [0, 3, 6],
    [3, 4, 5],
    [2, 4, 6],
    [1, 4, 7],
    [6, 7, 8],
    [2, 5, 8]
]

# Welcome to the game
print("Welcome to Tic Tac Toe game!")

# Choose type of game: with someone or with computer
correct_type = False
while not correct_type:
    game_type = input('Would you like to choose multiplayer mode (type "M") '
                      'or with the computer (type "C")? ').capitalize()
    if game_type == "M":
        # Ask names of players
        player_1_name = input("What is the name of the first player? ").capitalize()
        player_2_name = input("What is the name of the second player? ").capitalize()
        correct_type = True
        # Check who starts the game
        first_move = False
        while not first_move:
            first_dice = random.randint(1, 6)
            second_dice = random.randint(1, 6)
            input("First you need to throw a dice to check who will start the game. Press Enter for continue")
            input(f"{player_1_name}'s dice shows {first_dice}. Press Enter for continue")
            input(f"{player_2_name}'s dice shows {second_dice}. Press Enter for continue")
            if first_dice > second_dice:
                input(f"{player_1_name} is first. Press Enter for continue")
                first_move = True
                first = player_1_name
            elif second_dice > first_dice:
                input(f"{player_2_name} is first. Press Enter for continue")
                first_move = True
                first = player_2_name
            else:
                input("Throw dices one more time")
        # Choose the symbol for first player, second player will be chosen automatically
        correct_mark = False
        while not correct_mark:
            player_1 = input(f"Does {first} want to be 'X' or '0': ").capitalize()
            if player_1 == 'X':
                player_2 = '0'
                correct_mark = True
            elif player_1 == '0' or player_1 == "O":
                player_2 = 'X'
                correct_mark = True
            else:
                print("You've entered wrong symbol, please try again")
                player_2 = ''
    elif game_type == "C":
        player_1_name = input("What is the name of the first player? ").capitalize()
        player_2_name = "Computer"
        correct_type = True
        # Check who starts the game
        first_move = False
        while not first_move:
            first_dice = random.randint(1, 6)
            second_dice = random.randint(1, 6)
            input("First you need to throw a dice to check who will start the game. Press Enter for continue")
            input(f"{player_1_name}'s dice shows {first_dice}. Press Enter for continue")
            input(f"{player_2_name}'s dice shows {second_dice}. Press Enter for continue")
            if first_dice > second_dice:
                input(f"{player_1_name} is first. Press Enter for continue")
                first_move = True
                first = player_1_name
                correct_mark = False
                while not correct_mark:
                    player_1 = input(f"Does {first} want to be 'X' or '0': ").capitalize()
                    if player_1 == 'X':
                        player_2 = '0'
                        correct_mark = True
                    elif player_1 == '0' or player_1 == "O":
                        player_2 = 'X'
                        correct_mark = True
                    else:
                        print("You've entered wrong symbol, please try again")
                        player_2 = ''
            elif second_dice > first_dice:
                input(f"{player_2_name} is first. Press Enter for continue")
                first_move = True
                turn = 2
                first = player_2_name
                player_1 = "X"
                player_2 = '0'
            else:
                input("Throw dices one more time")

    else:
        print("You've entered wrong symbol, please try again")


def winner(user_turn):
    if user_turn == 2:
        print(f'Winner is {player_1_name}')
    else:
        print(f'Winner is {player_2_name}')


# Move function for multiplayer game
def move(user_turn):
    move_made = False
    while not move_made:
        if user_turn == 1:
            user_move = int(input(f"{player_1_name}'s move. Where do you want to move? "
                                  f"Choose a number between 1 to 9: "))
            if game_moves[user_move - 1] == " ":
                game_moves[user_move - 1] = player_1
                move_made = True
                user_turn = 2
                return user_turn
            else:
                print("This sell is already occupied. Please try again")
        else:
            user_move = int(input(f"{player_2_name}'s move. Where do you want to move? "
                                  f"Choose a number between 1 to 9: "))
            if game_moves[user_move - 1] == " ":
                game_moves[user_move - 1] = player_2
                move_made = True
                user_turn = 1
                return user_turn
            else:
                print("This sell is already occupied. Please try again")


# Check indices of first player
def list_duplicates_of(seq, item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item, start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs


# Check if computer can win
def computer_win(comp_positions):
    check = 0
    is_in = 0
    # Check if computer has two cells occupied from any of the winning positions, if yes -
    # choose missed number
    for position in range(len(winning_combos)):
        check += 1
        for comp in comp_positions:
            if comp in winning_combos[position]:
                is_in += 1
        # combo = winning_combos[cmb]
        if is_in < 2:
            is_in = 0
            if check == len(winning_combos):
                computer_move = False
                return computer_move
            # if combo is used - it is deleted from the winning positions combo list
        elif is_in == 2:
            combo = winning_combos[position]
            winning_combos.remove(combo)
            for i in combo:
                if i in comp_positions:
                    pass
                else:
                    computer_move = i
                    return computer_move


# Check if there are winning position for player
def player_win(x_positions):
    is_in = 0
    check = 0
    # Check if player 1 has two cells occupied from any of the winning positions, if yes -
    # choose missed number
    for alr in range(len(winning_combos)):
        check += 1
        for num in x_positions:
            if num in winning_combos[alr]:
                is_in += 1
        # combo = winning_combos[alr]
        if is_in < 2:
            is_in = 0
            if check == len(winning_combos):
                computer_move = random.randint(0, 8)
                return computer_move
        # if combo is used - it is deleted from the winning positions combo list
        elif is_in == 2:
            combo = winning_combos[alr]
            winning_combos.remove(combo)
            for char in combo:
                if char in x_positions:
                    pass
                else:
                    computer_move = char
                    return computer_move


# Move function for game with computer
def ai_move(user_turn):
    move_made = False
    while not move_made:
        # Player's move
        if user_turn == 1:
            user_move = int(input(f"{player_1_name}'s move. Where do you want to move? "
                                  f"Choose a number between 1 to 9: "))
            # Check if cell is not occupied
            if game_moves[user_move - 1] == " ":
                game_moves[user_move - 1] = player_1
                move_made = True
                user_turn = 2
                return user_turn
            else:
                print("This sell is already occupied. Please try again")
        # Computer's turn
        else:
            # Write all indeces where computer made move
            indices_comp = list_duplicates_of(game_moves, player_2)
            # Write all indeces where user player made move
            indices_x = list_duplicates_of(game_moves, player_1)
            correct_move = False
            while not correct_move:
                # First move is random if middle position is occupied
                if len(indices_comp) < 1:
                    if 4 in indices_x:
                        comp_move = random.randint(0, 8)
                    else:
                        comp_move = 4
                elif len(indices_comp) < 2:
                    comp_move = player_win(indices_x)
                elif len(indices_comp) == 2:
                    comp_move = computer_win(indices_comp)
                    if not comp_move:
                        comp_move = player_win(indices_x)
                else:
                    comp_move = player_win(indices_x)
                # check if cell is not occupied
                if game_moves[comp_move] == " ":
                    game_moves[comp_move] = player_2
                    move_made = True
                    correct_move = True
                    user_turn = 1
                    return user_turn


def show_field():
    game_field = (f' {game_moves[0]} | {game_moves[1]} | {game_moves[2]} \n'
                  f'-----------\n'
                  f' {game_moves[3]} | {game_moves[4]} | {game_moves[5]} \n'
                  f'-----------\n'
                  f' {game_moves[6]} | {game_moves[7]} | {game_moves[8]} ')
    return print(game_field)


is_end = False
# Create empty field
game_moves = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Multiplayer game
if game_type == "M":
    # Start game - while loop will be until is_end will become True
    turn = move(turn)

    # Show move on field
    field = (f' {game_moves[0]} | {game_moves[1]} | {game_moves[2]} \n'
             f'-----------\n'
             f' {game_moves[3]} | {game_moves[4]} | {game_moves[5]} \n'
             f'-----------\n'
             f' {game_moves[6]} | {game_moves[7]} | {game_moves[8]} ')
    os.system('cls')
    print(field)
    while not is_end:
        field = (f' {game_moves[0]} | {game_moves[1]} | {game_moves[2]} \n'
                 f'-----------\n'
                 f' {game_moves[3]} | {game_moves[4]} | {game_moves[5]} \n'
                 f'-----------\n'
                 f' {game_moves[6]} | {game_moves[7]} | {game_moves[8]} ')
        # Check if end is ended
        if ((game_moves[0] == game_moves[1] == game_moves[2] and game_moves[2] != " ") or
                (game_moves[0] == game_moves[4] == game_moves[8] and game_moves[4] != " ") or
                (game_moves[0] == game_moves[3] == game_moves[6] and game_moves[6] != " ") or
                (game_moves[3] == game_moves[4] == game_moves[5] and game_moves[4] != " ") or
                (game_moves[2] == game_moves[4] == game_moves[6] and game_moves[6] != " ") or
                (game_moves[1] == game_moves[4] == game_moves[7] and game_moves[4] != " ") or
                (game_moves[6] == game_moves[7] == game_moves[8] and game_moves[6] != " ") or
                (game_moves[2] == game_moves[5] == game_moves[8] and game_moves[2] != " ")):
            is_end = True
            winner(turn)

        # Check if draw
        elif " " not in game_moves:
            print("It's a draw. No more chances to move")
            is_end = True
        # Check make a move
        else:
            turn = move(turn)
            os.system('cls')
            show_field()
else:
    # Start game - while loop will be until is_end will become True
    turn = ai_move(turn)

    # Show move on field
    field = (f' {game_moves[0]} | {game_moves[1]} | {game_moves[2]} \n'
             f'-----------\n'
             f' {game_moves[3]} | {game_moves[4]} | {game_moves[5]} \n'
             f'-----------\n'
             f' {game_moves[6]} | {game_moves[7]} | {game_moves[8]} ')
    os.system('cls')
    print(field)
    while not is_end:
        field = (f' {game_moves[0]} | {game_moves[1]} | {game_moves[2]} \n'
                 f'-----------\n'
                 f' {game_moves[3]} | {game_moves[4]} | {game_moves[5]} \n'
                 f'-----------\n'
                 f' {game_moves[6]} | {game_moves[7]} | {game_moves[8]} ')
        # Check if end is ended
        if ((game_moves[0] == game_moves[1] == game_moves[2] and game_moves[2] != " ") or
                (game_moves[0] == game_moves[4] == game_moves[8] and game_moves[4] != " ") or
                (game_moves[0] == game_moves[3] == game_moves[6] and game_moves[6] != " ") or
                (game_moves[3] == game_moves[4] == game_moves[5] and game_moves[4] != " ") or
                (game_moves[2] == game_moves[4] == game_moves[6] and game_moves[6] != " ") or
                (game_moves[1] == game_moves[4] == game_moves[7] and game_moves[4] != " ") or
                (game_moves[6] == game_moves[7] == game_moves[8] and game_moves[6] != " ") or
                (game_moves[2] == game_moves[5] == game_moves[8] and game_moves[2] != " ")):
            is_end = True
            winner(turn)

        # Check if draw
        elif " " not in game_moves:
            print("It's a draw. No more chances to move")
            is_end = True
        # Check make a move
        else:
            turn = ai_move(turn)
            os.system('cls')
            show_field()
