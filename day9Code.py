import time

with open('day9Input.txt') as infile:
    numlst = infile.read().split('\n')
    numlst = list(map(int, numlst))

def sumCheck(inlist, i):
    if i < 25: return
    chklist = inlist[(i-25):i]
    #print(chklist)
    for num in chklist:
        #print(inlist[i], num, inlist[i]-num)
        if (inlist[i] - num) in chklist: return True
    return False

# Part 1
st = time.time()
for i in range(25, len(numlst)):
    if not sumCheck(numlst, i):
        #print(i, numlst[i])
        invalid = numlst[i]

finishstr = ' in ' + '%.4f' %(time.time() - st) + ' seconds'
print('Part 1: ', invalid, finishstr)

# Part 2
st = time.time()
for i, val in enumerate(numlst):
    contigSum = 0
    step = 0
    while contigSum < invalid:
        contigSum += numlst[i + step]
        step += 1
    if contigSum == invalid and step > 1:
        contigStart = i
        contigEnd = i + step - 1

if contigEnd and contigStart:
    contigMin = min(numlst[contigStart:contigEnd+1])
    contigMax = max(numlst[contigStart:contigEnd+1])
    #print(contigStart, contigEnd, contigMin, contigMax, contigMin + contigMax, sum(numlst[contigStart:contigEnd+1]))

finishstr = ' in ' + '%.4f' %(time.time() - st) + ' seconds'
print('Part 2: ', contigMax+contigMin, finishstr)