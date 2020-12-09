import numpy
import time

with open('day3Input.txt') as infile:
    data = infile.read().splitlines()

(xMax, yMax) = (len(data[0]), len(data))

#findTrees
def findTrees(funcdata, dx, dy):
    (x, y) = (0, 0)
    numTrees = 0
    while y < yMax:
        #print(x,y)
        if funcdata[y][x] == '#': numTrees += 1
        x = (x + dx) % xMax
        y += dy
    return numTrees


def findTrees2(funcdata, dx, dy):
    numTrees = 0
    for i, line in enumerate(funcdata[::dy]):
        if line[(i*dx) % len(line)] == '#': numTrees += 1
    return numTrees


#part 1
st = time.time()
Part1 = findTrees2(data, 3, 1)
print(Part1)
print("----%.4f----" % (time.time() - st))


#Part 2
st = time.time()
res=[]
for dx, dy in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    res.append(findTrees2(data, dx, dy))

Part2 = numpy.prod(res)
print(Part2)
print("----%.4f----" % (time.time() - st))

exit()