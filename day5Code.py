with open('day5Input.txt') as infile:
    datafile = infile.read().split('\n')

#rows 0 - 127 (128), columns 0-7
# 1, 2, 4, 8, 16, 32, 64 (2^6)

seatIDlist = []
#rows = []
#cols = []
for record in datafile:
    row = col = 0
    #print(record[0:7], '-', record[7:10])
    for i in range(0, 7):
        if record[i] == 'B': row += 2**(6-i)
        #print(row)
    for i in range(7, 10):
        if record[i] == 'R': col += 2**(2-(i-7))
    seatID = (row * 8) + col
    seatIDlist.append(seatID)
    #rows.append(row)
    #cols.append(col)

seatIDlist.sort()
print('Part 1: ', seatIDlist[-1])

seat = [id for id in range(seatIDlist[0], seatIDlist[-1] + 1) if id not in seatIDlist]
print('Part 2: ', seat[0])


