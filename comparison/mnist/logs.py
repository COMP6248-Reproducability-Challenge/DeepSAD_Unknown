import re

lis_all = []

with open('./mnist_param3_2/log.txt') as f:
    lis = f.readlines()
    count = 0
    for l in lis:
        pattern1 = re.compile(r'Test AUC: \d+.(\d+)')
        res1 = pattern1.search(l)
        if res1 :
            lis_all.append(float(res1.group(0).split(' ')[-1]))
print(lis_all)
print(len(lis_all))


