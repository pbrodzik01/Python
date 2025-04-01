import random

def generate_board(seed):
    random.seed(seed)
    board_size = 10
    board = [[0 for x in range(board_size)] for y in range(board_size)]
    ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    for ship_size in ship_sizes:
        while True:
            x, y = random.randint(0, board_size - 1), random.randint(0, board_size - 1)
            direction = random.choice(['horizontal', 'vertical'])
            if direction == 'horizontal' and x + ship_size <= board_size:
                invalid = False
                for i in range(x, x + ship_size):
                    if board[y][i] != 0 or (y > 0 and board[y - 1][i] != 0) or (y < board_size - 1 and board[y + 1][i] != 0) or (i > 0 and board[y][i - 1] != 0) or (i < board_size - 1 and board[y][i + 1] != 0):
                        invalid = True
                        break
                if not invalid:
                    for i in range(x, x + ship_size):
                        board[y][i] = ship_size     #DO DALSZEJ OBRÓBKI MOŻNA ZAMIENIĆ 'ship_size' NA '1'
                    break
            elif direction == 'vertical' and y + ship_size <= board_size:
                invalid = False
                for i in range(y, y + ship_size):
                    if board[i][x] != 0 or (x > 0 and board[i][x - 1] != 0) or (x < board_size - 1 and board[i][x + 1] != 0) or (i > 0 and board[i - 1][x] != 0) or (i < board_size - 1 and board[i + 1][x] != 0):
                        invalid = True
                        break
                if not invalid:
                    for i in range(y, y + ship_size):
                        board[i][x] = ship_size     #DO DALSZEJ OBRÓBKI MOŻNA ZAMIENIĆ 'ship_size' NA '1'
                    break
    return board


print('\x1b[38;2;255;0;0m'+"PROSZĘ PODAĆ ILOŚĆ PLANSZ"+'\x1b[0m')
while True:
    try:
        quantity = int(input("ILOŚĆ:   "))
        break
    except ValueError:
        print('\x1b[38;2;255;0;0m'+"COŚ POSZŁO NIE TAK! SPRÓBUJ PONOWNIE!"+'\x1b[0m')


for i in range(quantity):
    print('\x1b[38;2;255;0;0m' + f"\n\n----------------------------------" + '\x1b[0m')
    print('\x1b[38;2;255;0;0m' + f"GENEROWANIE PLANSZY NR {i+1}" + '\x1b[0m')

    print('\x1b[38;2;255;0;0m' + "\nPROSZĘ PODAĆ ZIARNO LOSOWOŚCI" + '\x1b[0m')
    while True:
        try:
            seed = int(input("ZIARNO:   "))
            break
        except ValueError:
            print('\x1b[38;2;255;0;0m' + "COŚ POSZŁO NIE TAK! SPRÓBUJ PONOWNIE!" + '\x1b[0m')

    print('\x1b[38;2;255;0;0m' + f"\nPLANSZA NR {i+1} ZOSTAŁA WYGENEROWANA:" + '\x1b[0m')

    boards = generate_board(seed)
    for board in boards:
        print(board)

    print('\x1b[38;2;255;0;0m' + f"----------------------------------" + '\x1b[0m')
