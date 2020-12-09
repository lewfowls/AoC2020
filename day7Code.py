import re
import time

with open('day7Input.txt') as f:
        datafile = f.read().splitlines()

reOuter = re.compile('^([\w ]*) bags contain ')
reInner = re.compile('(\d{1,}) ([\w ]*) bag(?:s)?')

rules = {}

for rule in datafile:
    #the outer bag
    outer = reOuter.findall(rule)[0]
    #create key of outer in rules dictionary
    rules[outer] = {}
    #find the colour and number of bags the outer bag holds (returns list of tuples (number, colour))
    inner = reInner.findall(rule)
    for bag in inner:
        rules[outer][bag[1]] = int(bag[0])

def lookIn(outerBag, trail):
    '''
    looks in outerBag for 'shiny gold'
    if it finds it, returns True, ending the recursion
    if it doesn't, function calls itself with each inner bag to check them
    trail keeps track of the bags we have already checked to avoid duplicating/looping
    '''

    if 'shiny gold' in rules[outerBag]:
        return True
    else:
        for innerBag in rules[outerBag]:
            if innerBag not in trail:
                trail.append(innerBag)
                if lookIn(innerBag, trail):
                    return True
        return False

#Part 1 result
st = time.time()
part1 = 0
for rule in rules:
    trail = []
    if lookIn(rule, trail):
        part1 += 1
    #print(rule, count, trail)
finishstr = ' in ' + '%.4f' % (time.time() - st) + ' seconds'
print('Part 1: ' , part1, finishstr)


def countBags(outerBag):
    '''
    counts how many bags inside of outer bag, and calls again on each of the bags inside resursively
    :param outerBag:
    :return: total numbers of nested bags
    '''
    count = 0
    if len(rules[outerBag]):
        for innerBag in rules[outerBag]:
            # add to count the number of innerbag inside outerbag
            count += rules[outerBag][innerBag]
            # add to count the number of bags inside each of innerbag * number of innerbag in outerbag (recursion)
            count += rules[outerBag][innerBag] * countBags(innerBag)
        return count
    else:
        return 0

#Part 2 results
st = time.time()
finishstr = ' in ' + '%.4f' % (time.time() - st) + ' seconds'
print('Part 2: ', countBags('shiny gold'), ' in ' + '%.4f' % (time.time() - st) + ' seconds')