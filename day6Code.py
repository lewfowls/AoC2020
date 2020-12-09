import re


allGroups = []
part1Sum = part2Sum = 0
groupSize = 0
groupDict = {}


with open('day6Input.txt', 'r') as infile:
    for line in infile:
        stripped_line = line.strip()
        #print(stripped_line)
        if stripped_line == '': #line break between groups, reset counters
            for element in groupDict.values():
                #print(element)
                if element == groupSize: part2Sum += 1

            part1Sum += len(groupDict)
            allGroups.append(groupDict)
            #print(groupSize, part1Sum, part2Sum, groupDict)
            groupDict = dict()
            groupSize = 0

        if re.match('[a-z]', stripped_line):
            groupSize += 1
            for element in stripped_line:
                if (element in groupDict.keys()) == False:
                    groupDict[element] = 1
                else: groupDict[element] += 1
            #print(groupSize)

print(part1Sum, part2Sum)