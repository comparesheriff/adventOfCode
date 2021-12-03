import os
current_dir=os.path.dirname(__file__)

def part_one():
    increases = -1
    lastDigit = float('-inf')
    with open(current_dir+"/input.txt",'r') as file:
        for line in file:
            if(float(line) > lastDigit):
                increases += 1
            lastDigit = float(line)
    print("Increases:",increases)

def part_two():
    with open(current_dir+"/input.txt",'r') as file:
        increases = -1
        lastSum = 0
        lines = [int(line) for line in file]
        for index, line in enumerate(lines):
            if(index < len(lines) - 2):
                print("Adding",line, lines[index+1], lines[index+2])
                currentSum = line + lines[index+1] + lines[index+2]
                if(currentSum > lastSum):
                    print("last sum was",lastSum,"current sum is", currentSum)
                    increases += 1
                lastSum = currentSum
        print(increases)


            

part_one()
part_two()