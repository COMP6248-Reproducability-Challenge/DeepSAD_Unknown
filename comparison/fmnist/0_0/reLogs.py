import re

lis_all_test = []
lis_all_train = []


with open('../0_4/log(1).txt') as f:
    lis = f.readlines()
    count = 0
    for l in lis:
        pattern1 = re.compile(r'Test AUC: \d+.(\d+)')
        res1 = pattern1.search(l)
        pattern2 = re.compile(r'\| AUC: \d+.(\d+)')
        res2 = pattern2.search(l)
        if res1:
            lis_all_test.append(float(res1.group(0).split(' ')[-1]))
        elif res2:
            lis_all_train.append(float(res2.group(0).split(' ')[-1]))
print(lis_all_test)
print(lis_all_train)
