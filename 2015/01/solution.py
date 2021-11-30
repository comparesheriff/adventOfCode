import os
current_dir=os.path.dirname(__file__)

def part_one():
    floor = 0
    with open(current_dir+"/input.txt",'r') as file:
        for line in file:
            for character in line:
                if character == '(':
                    floor += 1
                elif character == ')':
                    floor -= 1
    print("Final floor:",floor)

def part_two():
    floor = 0
    with open(current_dir+"/input.txt",'r') as file:
        for line in file:
            for position,character in enumerate(line,1):
                if character == '(':
                    floor += 1
                elif character == ')':
                    floor -= 1
                if(floor < 0):
                    print("Position:", position)
                    break

part_one()
part_two()