import os
current_dir=os.path.dirname(__file__)

def part_one():
    wholeNeeded = 0
    with open(current_dir+"/input.txt",'r') as file:
        for line in file:
            dimensions = [int(x) for x in line.split("x")]
            areas = [dimensions[0]*dimensions[1],dimensions[1]*dimensions[2],dimensions[0]*dimensions[2]]
            neededStuff = 2 * sum(areas) + min(areas)
            wholeNeeded += neededStuff
    print(wholeNeeded)        

def part_two():
    wholeNeeded = 0
    with open(current_dir+"/input.txt",'r') as file:
        for line in file:
            dimensions = [int(x) for x in line.split("x")]
            volume = dimensions[0] * dimensions[1] * dimensions[2]
            dimensions.remove(max(dimensions))
            smallestDistance = 2 * dimensions[0] + 2 * dimensions[1]
            neededStuff = volume + smallestDistance
            wholeNeeded += neededStuff
    print(wholeNeeded)        

part_one()
part_two()