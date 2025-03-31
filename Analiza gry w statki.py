import random
from collections import  Counter

file = open("raport.txt", "w+")

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
                    if board[y][i] != 0 or (y > 0 and board[y - 1][i] != 0) or (
                            y < board_size - 1 and board[y + 1][i] != 0) or (i > 0 and board[y][i - 1] != 0) or (
                            i < board_size - 1 and board[y][i + 1] != 0) or (
                            (y > 0 and i > 0) and board[y - 1][i - 1] != 0) or (
                            (y > 0 and i < board_size - 1) and board[y - 1][i + 1] != 0) or (
                            (y < board_size - 1 and i > 0) and board[y + 1][i - 1] != 0) or (
                            (y < board_size - 1 and i < board_size - 1) and board[y + 1][i + 1] != 0):
                        invalid = True
                        break
                if not invalid:
                    for i in range(x, x + ship_size):
                        board[y][i] = ship_size
                    break
            elif direction == 'vertical' and y + ship_size <= board_size:
                invalid = False
                for i in range(y, y + ship_size):
                    if board[i][x] != 0 or (x > 0 and board[i][x - 1] != 0) or (
                            x < board_size - 1 and board[i][x + 1] != 0) or (i > 0 and board[i - 1][x] != 0) or (
                            i < board_size - 1 and board[i + 1][x] != 0) or (
                            (i > 0 and x > 0) and board[i - 1][x - 1] != 0) or (
                            (i > 0 and x < board_size - 1) and board[i - 1][x + 1] != 0) or (
                            (i < board_size - 1 and x > 0) and board[i + 1][x - 1] != 0) or (
                            (i < board_size - 1 and x < board_size - 1) and board[i + 1][x + 1] != 0):
                        invalid = True
                        break
                if not invalid:
                    for i in range(y, y + ship_size):
                        board[i][x] = ship_size
                    break
    return board


def print_board(board):
    print('\x1b[38;2;255;0;0m' + f"----------------------------------" + '\x1b[0m')
    print("   " + "  ".join(str(i) for i in range(len(board))))
    for i, row in enumerate(board):
        print(str(i) + "  " + "  ".join("." if x == 0 else "X" if x < 0 else str(x) for x in row))


def get_shot(shots, hits):
    if hits:
        # Sprawdź okolice ostatniego trafionego pola
        x, y = hits[-1]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10 and (nx, ny) not in [(s[0], s[1]) for s in shots]:
                return nx, ny

    # Losowy strzał
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if (x, y) not in [(s[0], s[1]) for s in shots]:
            return x, y


def get_ships(board):
    ships = {}
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] > 0:
                size = board[y][x]
                if size not in ships:
                    ships[size] = [(y, x)]
                else:
                    ships[size].append((y, x))
    return ships


def shoot(board, x, y, ships):
    if board[y][x] == 0:
        board[y][x] = -1
        return False, False
    else:
        size = board[y][x]
        board[y][x] = -size
        if all(board[i][j] == -size for i, j in ships[size]):
            for i, j in ships[size]:
                board[i][j] = -2 * size
            del ships[size]
            return True, True
        else:
            return True, False


def play_game(board):
    shots = []
    ships = get_ships(board)
    shot_count = 0
    hits = []

    while True:
        x, y = get_shot(shots, hits)
        hit, sink = shoot(board, x, y, ships)
        shots.append((x, y, hit))
        shot_count += 1

        if hit:
            if sink:
                hits.clear()
            else:
                hits.append((x, y))

        if len(ships) == 0:
            print("\nLiczba strzałów:", shot_count)
            print_shots(shots)

            file.write("SHOTS: \n")
            shots_str = [str(item) for item in shots]
            file.write("\n".join(shots_str) + "\n")
            break


def print_shots(shots):
    print("\nStrzały:")
    for shot in shots:
        x, y, hit = shot
        print(f"({x}, {y}) - {'Trafiony' if hit else 'Nietrafiony'}")


def analyze_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    counter = Counter(line for line in lines if "SHOTS" not in line and "False" not in line)
    top_lines = counter.most_common(10)

    print('\x1b[38;2;255;0;0m' + f"-----------------------------------------" + '\x1b[0m')
    print('\x1b[38;2;255;0;0m' + f"10 najczęściej powtarzających się linii" + '\x1b[0m')
    print('\x1b[38;2;255;0;0m' + f"wśród 100 losowo wygenerowanych planszy:" + '\x1b[0m')
    print('\x1b[38;2;255;0;0m' + f"-----------------------------------------" + '\x1b[0m')
    for line, count in top_lines:
        print(f"Linia: {line}, Liczba wystąpień: {count}")


def main():
    for i in range(100):
        seed = random.randint(1, 1000)
        board = generate_board(seed)
        print('\x1b[38;2;255;0;0m' + f"\n\n----------------------------------" + '\x1b[0m')
        print('\x1b[38;2;255;0;0m' + f"***   GENEROWANIE PLANSZY NR {i+1}  ***" + '\x1b[0m')
        print_board(board)
        play_game(board)

        analyze_file("raport.txt")


if __name__ == "__main__":
    main()
