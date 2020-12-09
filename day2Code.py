import time

def left(string, chars):
    return string[:chars]

def right(string, chars):
    return string[chars+1:]

dict = {}

i = 0
with open('day2Input.txt', 'r') as f:
    for line in f:
        (a, b, pword) = line.split()
        b2 = left(b, 1)
        a2 = left(a, a.find('-'))
        a3 = right(a, a.find('-'))
        dict[i] = (a2, a3, b2, pword)
        i += 1

#Part 1
st = time.time()
(count, x, y) = (0, 0, 0)
for i in dict.keys():
    a = int(dict[i][0])
    b = int(dict[i][1])
    c = dict[i][3].count(dict[i][2])
    if c >= a: x = 1
    else: x = 0
    if c <= b: y = 1
    else: y = 0
    if x + y == 2: count += 1

print('Part 1: ', count)
print("----%.4f----" % (time.time() - st), 'sec')

#Part 2
st = time.time()
count = 0
for i in dict.keys():
    p1 = int(dict[i][0]) - 1
    p2 = int(dict[i][1]) - 1
    letter = dict[i][2]
    pword = dict[i][3]
    if p2 <= len(pword):
        if pword[p1] == letter and pword[p2] != letter: count += 1
        if pword[p1] != letter and pword[p2] == letter: count += 1
    #print(pword[p1], pword[p2], letter)

print('Part 2: ', count)
print("----%.4f----" % (time.time() - st), 'sec')

