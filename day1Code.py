from pandas import *
from matplotlib import pyplot as plt
import time

st = time.time()

#read in data
#input = read_csv('day1Input.txt', header = None)
inputfile = open('day1Input.txt', 'r')
input = inputfile.read()
inputlist = input.split(sep='\n')
# print(inputlist)
# print(type(inputlist))


n = len(inputlist)-1

inputlist = inputlist[:n]
data = list(map(int, inputlist))


# numsum = int
# numprod = int
# i_1 = int
# j_1 = int
# k_1 = int
#


# part 1 optimal
for i in data:
    if (2020 - i) in data:
        print(i, (2020-i), i*(2020-i))
        break

print("----%.2f----" % (time.time() - st))
st = time.time()

# #part 2 slow
# for i in range(0, n):
#     for j in range(0, n):
#         for k in range(0, n):
#             numsum = data[i] + data[j] + data[k]
#             if(numsum == 2020):
#                 numprod = data[i]*data[j]*data[k]
#                 print(data[i], data[j], data[k], numprod)
#                 break

# part 2 optimal
for i in data:
    for j in data:
        if (2020 - i - j) in data:
            print(i, j, (2020-i-j), i*j*(2020-i))
            print("----%.2f----" % (time.time() - st))
            exit()


