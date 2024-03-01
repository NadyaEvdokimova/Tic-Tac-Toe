import os

turn = 1
# Welcome to the game
print("Welcome to Tic Tac Toe game!")
# Choose the symbol for first player, second player will be chosen automatically
player_1 = input("Does first player want to be 'X' or '0': ").capitalize()
if player_1 == 'X':
    player_2 = '0'
elif player_1 == '0' or player_1 == "O":
    player_2 = 'X'
else:
    print("You've entered wrong symbol, please try again")
    player_2 = ''


def winner(user_turn):
    if user_turn == 2:
        print('Winner is the first player')
    else:
        print('Winner is the second player')


def move(user_turn):
    move_made = False
    while not move_made:
        if user_turn == 1:
            user_move = int(input("First player's move. Where do you want to move? Choose a number between 1 to 9: "))
            if game_moves[user_move - 1] == "":
                game_moves[user_move - 1] = player_1
                move_made = True
                user_turn = 2
                return user_turn
            else:
                print("This sell is already occupied. Please try again")
        else:
            user_move = int(input("Second player's move. Where do you want to move? Choose a number between 1 to 9: "))
            if game_moves[user_move - 1] == "":
                game_moves[user_move - 1] = player_2
                move_made = True
                user_turn = 1
                return user_turn
            else:
                print("This sell is already occupied. Please try again")


def show_field():
    game_field = (f' {game_moves[0]} | {game_moves[1]} | {game_moves[2]} \n'
                  f'-----------\n'
                  f' {game_moves[3]} | {game_moves[4]} | {game_moves[5]} \n'
                  f'-----------\n'
                  f' {game_moves[6]} | {game_moves[7]} | {game_moves[8]} ')
    return print(game_field)


is_end = False
# Create empty field
game_moves = ["", "", "", "", "", "", "", "", ""]

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
    if ((game_moves[0] == game_moves[1] == game_moves[2] and game_moves[2] != "") or
            (game_moves[0] == game_moves[4] == game_moves[8] and game_moves[4] != "") or
            (game_moves[0] == game_moves[3] == game_moves[6] and game_moves[6] != "") or
            (game_moves[3] == game_moves[4] == game_moves[5] and game_moves[4] != "") or
            (game_moves[2] == game_moves[4] == game_moves[6] and game_moves[6] != "") or
            (game_moves[1] == game_moves[4] == game_moves[7] and game_moves[4] != "") or
            (game_moves[6] == game_moves[7] == game_moves[8] and game_moves[6] != "") or
            (game_moves[2] == game_moves[5] == game_moves[8] and game_moves[2] != "")):
        is_end = True
        winner(turn)

    # Check if draw
    elif "" not in game_moves:
        print("It's a draw. No more chances to move")
        is_end = True
    # Check make a move
    else:
        turn = move(turn)
        os.system('cls')
        show_field()




