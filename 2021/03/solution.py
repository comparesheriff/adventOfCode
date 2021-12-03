import os
current_dir=os.path.dirname(__file__)

def part_one():
    with open(current_dir+"/input.txt",'r') as file:
        count = 0
        allBits = []
        for line in file:
            singleBits = [int(x) for x in str(line) if x != "\n"]
            count += 1
            allBits.append(singleBits)
        final = [sum(i) for i in zip(*allBits)] 
        half = count / 2
        epsilon = ""
        gamma = ""
        for i in final:
            gamma += "1" if i >= half else "0"
            epsilon += "0" if i >= half else "1"
        print(final, count, gamma, epsilon)
        print("Gamma:",int(gamma,2))
        print("Epsilon:",int(epsilon,2))
        print("Factor:",int(gamma,2) * int(epsilon,2))

def part_two():
    gamma=""
    epsilon=""
    with open(current_dir+"/input.txt",'r') as file:
        allBits = []
        for line in file:
            singleBits = [int(x) for x in str(line) if x != "\n"]
            allBits.append(singleBits)
        final = [sum(i) for i in zip(*allBits)] 
        half = len(allBits) / 2
        gamma += "1" if final[0] >= half else "0"
        epsilon += "0" if final[0] >= half else "1"
        found=False
        filteredGammaBits = allBits
        filteredEpsilonBits = allBits
        while not (len(filteredGammaBits) == 1 and len(filteredEpsilonBits) == 1):
            if(len(filteredGammaBits) != 1):
                currentIndex=len(gamma)-1
                newFiltered = []
                print("POS G:", currentIndex)
                
                for bits in filteredGammaBits: 
                    if bits[currentIndex] == int(gamma[-1]):
                        newFiltered.append(bits)
                filteredGammaBits = newFiltered
                print("FILTERED G:",filteredGammaBits)
                if(len(filteredGammaBits) != 1):
                    finalGamma = [sum(i) for i in zip(*filteredGammaBits)]
                    print("FINAL G",finalGamma,len(filteredGammaBits))
                    gamma += "1" if finalGamma[currentIndex+1] >= len(filteredGammaBits) / 2 else "0"
                    print("GAMMA:",gamma)
            if(len(filteredEpsilonBits) != 1):
                currentIndex=len(epsilon)-1
                newFiltered = []
                print("POS E:", currentIndex)
                for bits in filteredEpsilonBits: 
                    if bits[currentIndex] == int(epsilon[-1]):
                        newFiltered.append(bits)
                filteredEpsilonBits = newFiltered
                print("FILTERED E",filteredEpsilonBits)
                if(len(filteredEpsilonBits) != 1):
                    finalEpsilon = [sum(i) for i in zip(*filteredEpsilonBits)]
                    print("FINAL E",finalEpsilon,len(filteredEpsilonBits))
                    epsilon += "0" if finalEpsilon[currentIndex+1] >= len(filteredEpsilonBits) / 2 else "1"
                    print("EPSILON:",epsilon)

        oxy=""
        co=""
        for i in filteredGammaBits[0]:
            oxy += str(i)
        for i in filteredEpsilonBits[0]:
            co += str(i)
        print(oxy,co,int(oxy,2)*int(co,2))

part_one()
part_two()