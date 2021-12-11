import os
import sys
current_dir=os.path.dirname(__file__)

def part_one():
    with open(current_dir+"/input.txt",'r') as file:
        for line in file:
            crabs = [int(x) for x in line.split(",")]
            min_distance = sys.maxsize
            for position in range(min(crabs),max(crabs)+1):
                distance = 0
                for crab_position in crabs:
                    distance += abs(crab_position-position)
                if(distance < min_distance): min_distance = distance
            return min_distance

def part_two():
    with open(current_dir+"/input.txt",'r') as file:
        for line in file:
            crabs = [int(x) for x in line.split(",")]
            min_distance = sys.maxsize
            for position in range(min(crabs),max(crabs)+1):
                distance = 0
                for crab_position in crabs:
                    distance += sum(range(abs(crab_position-position)+1))
                if(distance < min_distance): min_distance = distance
            return min_distance

print(part_one())
print("---")
print(part_two())