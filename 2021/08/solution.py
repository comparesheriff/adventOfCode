import os
import sys
import time
current_dir=os.path.dirname(__file__)

def part_one():
    with open(current_dir+"/input.txt",'r') as file:
        count = 0
        for line in file:
            outputs = line.split("|")[1].strip().split(" ")
            for output in outputs:
                if len(output) in [2,3,4,7]:
                    count += 1
        return count

def part_two():
    seven_segment = {"abcefg":0,"cf":1,"acdeg":2,"acdfg":3,"bcdf":4,"abdfg":5,"abdefg":6,"acf":7,"abcdefg":8,"abcdfg":9}    
    with open(current_dir+"/input.txt",'r') as file:
        count = 0
        for line in file:
            inputs = sorted(line.split("|")[0].strip().split(" "), key=len)
            outputs = [''.join(sorted(x)) for x in line.split("|")[1].strip().split(" ")]
            code = dict()
            one_candidates = []
            four_candidates = []
            eight_candidates = []
            while len(code.keys()) < 7:
                for current_input in inputs:
                    if len(current_input) == 2:
                        one_candidates = list(current_input)
                    if (len(current_input) == 3 and len(one_candidates) > 0):
                        for x in current_input:
                            if x not in one_candidates:
                                code[x]="a"
                    if (len(current_input) == 4 and len(one_candidates) > 0):
                        for x in current_input:
                            if x not in one_candidates and x not in four_candidates:
                                four_candidates.append(x)
                    if (len(current_input) == 7 and len(one_candidates) > 0 and len(four_candidates) > 0):
                        for x in current_input:
                            if x != get_key("a", code) and x not in one_candidates and x not in four_candidates and x not in eight_candidates:
                                eight_candidates.append(x)
                    if (len(current_input) == 5 and len(one_candidates) > 0 and len(four_candidates) > 0) and len(eight_candidates) > 0 and "a" in code.values():
                        if(get_key("a", code) in current_input and all(x in current_input for x in one_candidates)): #this is the three
                            for x in current_input:
                                if(x != get_key("a", code) and x not in one_candidates):
                                    if x in four_candidates:
                                        code[x] = "d"
                                        for i in four_candidates:
                                            if i != x:
                                                code[i] = "b"
                                    elif x in eight_candidates:
                                        code[x] = "g"
                                        for i in eight_candidates:
                                            if i != x:
                                                code[i] = "e"
                        if(get_key("a", code) in current_input and get_key("d", code) in current_input and get_key("e", code) in current_input and get_key("g", code) in current_input):
                            for x in current_input:
                                if x != get_key("a", code) and x != get_key("d", code) and x != get_key("e", code) and x != get_key("g", code):
                                    code[x] = "c"
                                    for i in one_candidates:
                                        if i != x:
                                            code[i] = "f"
            print(code)
            output_string = ""
            for output in outputs:
                decoded = ""
                for i in output:
                    decoded += code[i]
                sorted_decoded = ''.join(sorted(decoded))
                output_string += str(seven_segment[sorted_decoded])
            count += int(output_string)
        return count

def get_key(val, my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key
 
    return "zzz"

print(part_one())
print("---")
print(part_two())