
def get_input():
    with open('day04.txt', 'r') as file:
        nums = [int(n) for n in file.readline().strip().split(',')]
        rest = [line.strip() for line in file.readlines() if line.strip() is not ""]

    boards = []
    y = 0
    board = [[]]
    for line in rest:
        z = [n.strip() for n in line.split(' ') if n]
        for x, num in enumerate(z):
            board[y].append(int(num))
        y += 1
        if y % 5 != 0:
            board.append([])
        else:
            boards.append(board[:])
            y = 0
            board = [[]]
            
    return nums, boards


def call_number(board, num):
    for row in board:
        for x, square in enumerate(row):
            if square == num:
                row[x] = None


def check_board(board):
    # horizontal bingo
    for y in range(5):
        bingo = True
        for x in range(5):
            if board[y][x] is not None:
                bingo = False
                break
        if bingo:
            return True

    # vertical bingo
    for x in range(5):
        bingo = True
        for y in range(5):
            if board[y][x] is not None:
                bingo = False
                break
        if bingo:
            return True

    return False


def print_board(board):
    for row in board:
        for n in row:
            if n is None:
                out = "_"
            else:
                out = str(n)
            out = out.rjust(3)
            print(out, end="")
        print()
    print()


def sum_board(board):
    sum = 0
    for row in board:
        for n in row:
            if n is not None:
                sum += n
    return sum


def day4a():
    print("    Part A")
    nums, boards = get_input()
    for num in nums:
        for board in boards:
            call_number(board, num)
        for board in boards:
            if (check_board(board)):
                print("Bingo!")
                print_board(board)
                print(sum_board(board) * num)
                return


def day4b():
    print("\n    Part B")
    nums, boards = get_input()
    last_board = None
    last_num = 0
    to_remove = []
    for num in nums:
        for board in boards:
            call_number(board, num)
        for i, board in enumerate(boards):
            if check_board(board):
                last_board = board
                last_num = num
                to_remove.append(i)
        if to_remove:
            to_remove.sort(reverse=True)
            for idx in to_remove:
                boards.pop(idx)
            to_remove = []

    print("Losing board:")
    print_board(last_board)
    print(sum_board(last_board) * last_num)


if __name__ == '__main__':
    day4a()
    day4b()
