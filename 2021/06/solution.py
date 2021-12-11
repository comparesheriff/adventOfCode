import os
current_dir=os.path.dirname(__file__)

def part_one():
    with open(current_dir+"/input.txt",'r') as file:
        for line in file:
            fishes = line.split(",")
            fish_dict = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0}
            for fish in fishes:
                fish_dict[fish] = fish_dict[fish] + 1
            
            for i in range(80):
                zeroes = fish_dict["0"]
                print(i, fish_dict, zeroes)
                fish_dict["0"] = fish_dict["1"]
                fish_dict["1"] = fish_dict["2"]
                fish_dict["2"] = fish_dict["3"]
                fish_dict["3"] = fish_dict["4"]
                fish_dict["4"] = fish_dict["5"]
                fish_dict["5"] = fish_dict["6"]
                fish_dict["6"] = fish_dict["7"] + zeroes
                fish_dict["7"] = fish_dict["8"]
                fish_dict["8"] = zeroes
            return sum(fish_dict.values())

def part_two():
    with open(current_dir+"/input.txt",'r') as file:
        for line in file:
            fishes = line.split(",")
            fish_dict = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0}
            for fish in fishes:
                fish_dict[fish] = fish_dict[fish] + 1
            
            for i in range(256):
                zeroes = fish_dict["0"]
                print(i, fish_dict, zeroes)
                fish_dict["0"] = fish_dict["1"]
                fish_dict["1"] = fish_dict["2"]
                fish_dict["2"] = fish_dict["3"]
                fish_dict["3"] = fish_dict["4"]
                fish_dict["4"] = fish_dict["5"]
                fish_dict["5"] = fish_dict["6"]
                fish_dict["6"] = fish_dict["7"] + zeroes
                fish_dict["7"] = fish_dict["8"]
                fish_dict["8"] = zeroes
            return sum(fish_dict.values())

print(part_one())
print("---")
print(part_two())