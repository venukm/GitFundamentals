# Validate board 
def validate_board(board):
    if len(board) != 9 or type(board) != list:
        raise ValueError("Not a tic tac toe board!")


# Display board
def display_board(board):
    
    validate_board(board)
    
    for val in range(0, 9):
        print('{0} '.format(board[val]), end = '')
        
        if (val + 1) % 3 == 0:
            print('\n')

# Determine win status
def win_status(board):
    
    validate_board(board)

    if (
        board[0] == board[1] == board[2] or
        board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6]
    ):
        return True
    else:
        return False


class player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


player_name = input('Input name of first player : ')
player_1 = player(player_name, 'x')
print('Your symbol is x')
player_name = input('Input name of second playes : ')
player_2 = player(player_name, 'o')
print('Your symbol is o')

# Set tic tac toe board
t_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

player_turn = 0
player_symbol = None
available_positions = None

while True:
    display_board(t_board)

    available_positions = [i for i in t_board if i not in ['x', 'o']]
    
    if len(available_positions) == 0:
        print("Game Over! Draw!")
        break
    
    if player_turn % 2 == 0:
        position = input('{0} - Select an available position : '.format(player_1.name.title()))
        player_symbol = 'x'
    else:
        player_symbol = 'o'
        position = input('{0} - Select an available position : '.format(player_2.name.title()))

    if position not in available_positions:
        print("Please select a valid position")
        continue
    
    t_board[t_board.index(position)] = player_symbol

    if win_status(t_board) == True:
        display_board(t_board)

        if player_turn % 2 == 0:
            print("Game Over! {0} is the winner!".format(player_1.name.title()))
        else:
            print("Game Over! {0} is the winner!".format(player_2.name.title()))
        
        break

    player_turn += 1
    