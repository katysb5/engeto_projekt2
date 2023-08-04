"""
projekt_2.py: TIC TAC TOE - druhý projekt do Engeto Online Python Akademie
author: Katerina Novakova
email: katule.novakova@email.cz
discord: katysb5#4067
"""
MOVES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
TAKEN_MOVES = []
start = 15
next_row = 22
box = 2

# zde kontroluji, zda hracem zvoleny tah, patri mezi povolene tahy
def check_input(move):
    if move not in MOVES:
        print("Wrong input, please try again: ")
        move = input()
        new_move = check_input(move)
    else:
        return move
    return new_move

# zde vytvarim novy grid na zaklade prave zadaneho tahu hracem
def get_new_grid(move, symbol, grid):
    if move in TAKEN_MOVES:
        print("This place is already taken, try again: ")
        move = input()
        new_move = check_input(move)
        get_new_grid(new_move, symbol, grid)
    elif move == MOVES[0]:
        grid[start] = symbol
    elif move == MOVES[1]:
        grid[start + box] = symbol
    elif move == MOVES[2]:
        grid[start + (2 * box)] = symbol
    elif move == MOVES[3]:
        grid[start + next_row] = symbol
    elif move == MOVES[4]:
        grid[start + next_row + box] = symbol
    elif move == MOVES[5]:
        grid[start + next_row + (2 * box)] = symbol
    elif move == MOVES[6]:
        grid[start + (2 * next_row)] = symbol
    elif move == MOVES[7]:
        grid[start + (2 * next_row) + box] = symbol
    else:
        grid[start + (2 * next_row) + (2 * box)] = symbol
    TAKEN_MOVES.append(move)
    return grid

# zde kontroluji, zda nektery hrac uz nedosahl vitezstvi
def check_for_victory(symbol, grid):
    if grid[start] == symbol and grid[start + box] == symbol and grid[start + (2 * box)] == symbol:
        return True
    elif grid[start + next_row] == symbol and grid[start + next_row + box] == symbol and grid[start + next_row + (2 * box)] == symbol:
        return True
    elif grid[start + (2 * next_row)] == symbol and grid[start + (2 * next_row) + box] == symbol and grid[start + (2 * next_row) + (2 * box)] == symbol:
        return True
    elif grid[start] == symbol and grid[start + next_row] == symbol and grid[start + (2 * next_row)] == symbol:
        return True
    elif grid[start + box] == symbol and grid[start + next_row + box] == symbol and grid[start + (2 * next_row) + box] == symbol:
        return True
    elif grid[start + (2 * box)] == symbol and grid[start + next_row + (2 * box)] == symbol and grid[start + (2 * next_row) + (2 * box)] == symbol:
        return True
    elif grid[start] == symbol and grid[start + next_row + box] == symbol and grid[start + (2 * next_row) + (2 * box)] == symbol:
        return True
    elif grid[start + (2 * box)] == symbol and grid[start + next_row + box] == symbol and grid[start + (2 * next_row)] == symbol:
        return True
    return False

print("Welcome to Tic Tac Toe")
print("========================================")
print("GAME RULES:")
print("Each player can place one mark (or stone)")
print("per turn on the 3x3 grid. The WINNER is")
print("who succeeds in placing three of their")
print("marks in a:\n* horizontal,\n* vertical or\n* diagonal row")
print("Let's start the game")
print("--------------------------------------------")

victory = False
# u toho gridu si uvedomuji, ze by to slo udelat asi nejak lepe, aby se to dalo
# potom lepe aktualizovat treba pri zvetseni gridu, ci tak, ale ja jsem tento
# projekt chtela udelat bez extra googleni, ciste jen z mych znalosti a toto
# je to "nejlepsi" co me napadlo
empty_grid = ['+', '-', '-', '-', '+', '-', '-', '-', '+', '-', '-', '-',\
            '+', '\n', '|', '   ', '|', '   ', '|', '   ', '|', '\n', '+',\
            '-', '-', '-', '+', '-', '-', '-', '+', '-', '-', '-', '+', '\n',\
            '|', '   ', '|', '   ','|', '   ', '|', '\n', '+', '-', '-', '-',\
            '+', '-', '-', '-', '+', '-', '-', '-', '+', '\n', '|', '   ',\
            '|', '   ', '|', '   ', '|', '\n', '+', '-', '-', '-', '+', '-',\
            '-', '-', '+', '-', '-', '-', '+', '\n']
round = 0
move = ""
symbol = ""

print(''.join(empty_grid))

while(victory == False):
    if (round % 2 == 0):
        print("Player o | Please enter your move number (pick from numbers 1 - 9): ")
        symbol = " O "
    else:
        print("Player x | Please enter your move number (pick from numbers 1 - 9): ")
        symbol = " X "
    move = input()
    checked_move = check_input(move)
    new_grid = get_new_grid(checked_move, symbol, empty_grid)
    grid = new_grid
    print(''.join(grid))
    victory = check_for_victory(symbol, grid)
    if (len(TAKEN_MOVES) == 9 and victory == False):
        print("It's a draw!")
        break
    round += 1

print(''.join(grid))
if (round - 1) % 2 == 0 and victory:
    print("Congratulations! Player 0 won!")
elif round % 2 == 0 and victory:
    print("Congratulations! Player x won!")
else:
    print("Game Over!")
