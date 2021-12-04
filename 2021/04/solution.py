import os
current_dir=os.path.dirname(__file__)

def part_one():
    called_numbers = []
    boards = []
    with open(current_dir+"/input.txt",'r') as file:
        board_count = 0
        current_board = []
        for line_nr, line in enumerate(file,1):
            if(line_nr == 1):
                called_numbers = line.strip().split(",")
                continue
            if(" " in line and board_count < 5):
                current_board.append([(x, False) for x in line.strip().split(" ") if x.strip() != ""])
                board_count += 1
            if(board_count == 5):
                boards.append(current_board)
                board_count = 0
                current_board = []
    #print(boards)
    for called_number in called_numbers:
        for board in boards:
            for row_number, row in enumerate(board):
                for column_number, elem in enumerate(row):
                    if elem[0] == called_number:
                        board[row_number][column_number] = (elem[0],True)
                        #print("BOARD START")
                        #print(board[0][0][1],board[0][1][1],board[0][2][1],board[0][3][1],board[0][4][1])
                        #print(board[1][0][1],board[1][1][1],board[1][2][1],board[1][3][1],board[1][4][1])
                        #print(board[2][0][1],board[2][1][1],board[2][2][1],board[2][3][1],board[2][4][1])
                        #print(board[3][0][1],board[3][1][1],board[3][2][1],board[3][3][1],board[3][4][1])
                        #print(board[4][0][1],board[4][1][1],board[4][2][1],board[4][3][1],board[4][4][1])
                        #print("BOARD END")
                        column_finished = board[0][column_number][1] and board[1][column_number][1] and board[2][column_number][1] and board[3][column_number][1] and board[4][column_number][1]
                        row_finished = board[row_number][0][1] and board[row_number][1][1] and board[row_number][2][1] and board[row_number][3][1] and board[row_number][4][1]
                        if column_finished or row_finished:
                            #print("FINISHED:", called_number)
                            #print(board)
                            unmarked = 0
                            for board_row in board:
                                for row_elem in board_row:
                                    if not row_elem[1]:
                                        unmarked += int(row_elem[0])
                            return unmarked * int(called_number)





def part_two():
    called_numbers = []
    boards = []
    with open(current_dir+"/input.txt",'r') as file:
        board_count = 0
        current_board = []
        for line_nr, line in enumerate(file,1):
            if(line_nr == 1):
                called_numbers = line.strip().split(",")
                continue
            if(" " in line and board_count < 5):
                current_board.append([(x, False) for x in line.strip().split(" ") if x.strip() != ""])
                board_count += 1
            if(board_count == 5):
                boards.append(current_board)
                board_count = 0
                current_board = []
    len_numbers = len(called_numbers)
    last_won_board = []
    last_called_number = 0
    all_numbers_called = False
    board_won = False
    while not all_numbers_called:
        before = len(boards)
        for number_index, called_number in enumerate(called_numbers, 0):
            for board_number, board in enumerate(boards, 1):
                for row_number, row in enumerate(board):
                    for column_number, elem in enumerate(row):
                        if elem[0] == called_number:
                            board[row_number][column_number] = (elem[0],True)
                            #print("BOARD START")
                            #print(board[0][0][1],board[0][1][1],board[0][2][1],board[0][3][1],board[0][4][1])
                            #print(board[1][0][1],board[1][1][1],board[1][2][1],board[1][3][1],board[1][4][1])
                            #print(board[2][0][1],board[2][1][1],board[2][2][1],board[2][3][1],board[2][4][1])
                            #print(board[3][0][1],board[3][1][1],board[3][2][1],board[3][3][1],board[3][4][1])
                            #print(board[4][0][1],board[4][1][1],board[4][2][1],board[4][3][1],board[4][4][1])
                            #print("BOARD END")
                            column_finished = board[0][column_number][1] and board[1][column_number][1] and board[2][column_number][1] and board[3][column_number][1] and board[4][column_number][1]
                            row_finished = board[row_number][0][1] and board[row_number][1][1] and board[row_number][2][1] and board[row_number][3][1] and board[row_number][4][1]
                            if (column_finished or row_finished):
                                #print("FINISHED", board_number)
                                last_won_board = board
                                last_called_number = called_number
                                #print(boards)
                                boards.remove(board)
                                #print(boards)
                                board_won = True
                        if board_won: break
                    if board_won: break
                if board_won: break
            if board_won : 
                board_won = False
                #print("BOARD RESET")
                break
        if(len(boards) == before):
            #print("BOARD KEPT LENGTH")
            all_numbers_called = True
        
    unmarked = 0
    for board_row in last_won_board:
        #print(board_row)
        for row_elem in board_row:
            if not row_elem[1]:
                unmarked += int(row_elem[0])
    #print(unmarked, last_called_number)
    return unmarked * int(last_called_number)

print(part_one())
print("---")
print(part_two())