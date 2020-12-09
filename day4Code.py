import re
import time
with open('day4Input.txt') as infile:
    datafile = infile.read().split('\n\n')

keylist = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eyecols = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
#cid optional


def check_elements1(data, keys):
    count = 0
    for passport in data:
        elements = re.split('\n| |', passport)
        dic = dict(element.split(':') for element in elements)
        if all(key in dic for key in keys): count +=1
    return count

def check_elements2(data, keys, eyecols):
    count = 0
    for passport in data:
        elements = re.split('\n| |', passport)
        dic = dict(element.split(':') for element in elements)

        if all(key in dic for key in keys):

            rules = [
            1920 <= int(dic['byr']) <= 2002,
            2010 <= int(dic['iyr']) <= 2020,
            2020 <= int(dic['eyr']) <= 2030,
            2010 <= int(dic['iyr']) <= 2020,
            (dic['hgt'].endswith('cm') and 150 <= int(dic['hgt'][:-2]) <= 193) or (dic['hgt'].endswith('in') and 59 <= int(dic['hgt'][:-2]) <= 76),
            bool(re.fullmatch(r'#[0-9a-f]{6}', dic['hcl'])),
            dic['ecl'] in eyecols,
            bool(re.fullmatch(r'[0-9]{9}', dic['pid']))
            ]

            if all(rules): count += 1
    return count

st = time.time()
part1 = check_elements1(datafile, keylist)
finishstr = ' in ' + '%.4f' % (time.time() - st) + ' seconds'
print('Part 1: ', part1, finishstr )

st = time.time()
part2 = check_elements2(datafile, keylist, eyecols)
finishstr = ' in ' + '%.4f' % (time.time() - st) + ' seconds'
print('Part 2: ', part2, finishstr )
#print(dic)