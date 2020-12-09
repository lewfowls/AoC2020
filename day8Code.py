import time
import copy

boot = {}
i = 0
with open('day8Input.txt') as infile:
    #import text file with split
    for line in infile:
        boot[i] = line.split()
        i += 1

#create empty list with same number of elements []*infile
#for each operation in infile list, check new list element doesn't exist, new list element = acc value, then do next, return acc if new list element already exists

def bootProcess(bootfile):
    flag = line = accum = 0
    bootlist = [0]*len(bootfile)
    while flag < 1000:
        if line == len(bootfile): return ('Part 2: ' + str(accum))
        elif bootlist[line] > 0: return ('Part 1: ' + str(accum))
        elif bootfile[line][0] == 'jmp': line += int(bootfile[line][1])
        elif bootfile[line][0] == 'nop': line += 1
        elif bootfile[line][0] == 'acc':
            accum += int(bootfile[line][1])
            bootlist[line] = accum
            line += 1
        else:
            return('error')
        flag += 1

# Part 1
st = time.time()
print(bootProcess(boot), ' in ' + '%.4f' % (time.time() - st) + ' seconds')

# Part 2
st = time.time()
for i in range(len(boot)):
    boot2 = copy.deepcopy(boot)
    if boot2[i][0] == 'nop': boot2[i][0] = 'jmp'
    elif boot2[i][0] == 'jmp': boot2[i][0] = 'nop'
    outcome = bootProcess(boot2)
    if outcome[0:6] == 'Part 2':
        print(outcome, 'with item ', i, ' in ' + '%.4f' % (time.time() - st) + ' seconds')
        break