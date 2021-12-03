import os
current_dir=os.path.dirname(__file__)

def part_one():
    depth = 0
    position = 0
    with open(current_dir+"/input.txt",'r') as file:
        for line in file:
            split = line.split(" ")
            command = split[0]
            amount = int(split[1])
            if command == "forward":
                position += amount
            elif command == "down":
                depth += amount
            elif command == "up":
                depth -= amount
    print("depth",depth,",position",position,",multiplied",depth*position)

def part_two():
    depth = 0
    position = 0
    aim = 0
    with open(current_dir+"/input.txt",'r') as file:
        for line in file:
            split = line.split(" ")
            command = split[0]
            amount = int(split[1])
            if command == "forward":
                position += amount
                depth += amount * aim
            elif command == "down":
                aim += amount
            elif command == "up":
                aim -= amount
    print("depth",depth,",position",position,",multiplied",depth*position)

part_one()
part_two()