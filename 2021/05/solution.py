import os
current_dir=os.path.dirname(__file__)

def part_one():
    #board = [[0]*1000]*1000
    board = dict()
    count_multiples = 0
    with open(current_dir+"/input.txt",'r') as file:
        for line in file:
            first = line.split(" ")[0]
            first_x = int(first.strip().split(",")[0])
            first_y = int(first.strip().split(",")[1])
            second = line.split(" ")[2]
            second_x = int(second.strip().split(",")[0])
            second_y = int(second.strip().split(",")[1])
            if not (first_x == second_x or first_y == second_y): continue
            if first_y == second_y:
                smaller = min([first_x,second_x])
                bigger = max([first_x,second_x])
                for x in range(smaller,bigger+1):
                    if str(first_y)+"-"+str(x) in board.keys():
                        count = board[str(first_y)+"-"+str(x)]
                        board[str(first_y)+"-"+str(x)] = count + 1
                    else:
                        board[str(first_y)+"-"+str(x)] = 1
                continue
            if first_x == second_x:
                smaller = min([first_y,second_y])
                bigger = max([first_y,second_y])
                for y in range(smaller,bigger+1):
                    if str(y)+"-"+str(first_x) in board.keys():
                        count = board[str(y)+"-"+str(first_x)]
                        board[str(y)+"-"+str(first_x)] = count + 1
                    else:
                        board[str(y)+"-"+str(first_x)] = 1
                continue
    for key,value in board.items():
        if(value > 1):
            count_multiples += 1
    return count_multiples

def part_two():
    board = dict()
    count_multiples = 0
    with open(current_dir+"/input.txt",'r') as file:
        for line in file:
            #split each line into the coordinates (and clean up, parse to int)
            first = line.split(" ")[0]
            first_x = int(first.strip().split(",")[0])
            first_y = int(first.strip().split(",")[1])
            second = line.split(" ")[2]
            second_x = int(second.strip().split(",")[0])
            second_y = int(second.strip().split(",")[1])
            # HORIZONTAL LINE
            if first_y == second_y:
                smaller = min([first_x,second_x])
                bigger = max([first_x,second_x])
                for x in range(smaller,bigger+1):
                    if str(first_y)+"-"+str(x) in board.keys():
                        count = board[str(first_y)+"-"+str(x)]
                        board[str(first_y)+"-"+str(x)] = count + 1
                    else:
                        board[str(first_y)+"-"+str(x)] = 1
                continue
            if first_x == second_x:
                smaller = min([first_y,second_y])
                bigger = max([first_y,second_y])
                for y in range(smaller,bigger+1):
                    if str(y)+"-"+str(first_x) in board.keys():
                        count = board[str(y)+"-"+str(first_x)]
                        board[str(y)+"-"+str(first_x)] = count + 1
                    else:
                        board[str(y)+"-"+str(first_x)] = 1
                continue
            # DIAGONAL LINES (because of the 45 degrees the absolute diff in each step has to be the same for x and y)
            elif abs(first_x-second_x) == abs(first_y-second_y):
                diff = abs(first_y - second_y)
                direction_x =  1 if first_x < second_x else -1
                direction_y =  1 if first_y < second_y else -1
                for diff_count in range(0, diff+1):
                    #add diff_count if we increase the coord, subtract if we decrease
                    x = first_x + (direction_x * diff_count)
                    y = first_y + (direction_y * diff_count)
                    
                    if str(y)+"-"+str(x) in board.keys():
                        count = board[str(y)+"-"+str(x)]
                        board[str(y)+"-"+str(x)] = count + 1
                    else:
                        board[str(y)+"-"+str(x)] = 1
                continue
    for key,value in board.items():
        if(value > 1):
            count_multiples += 1
    return count_multiples

print(part_one())
print("---")
print(part_two())