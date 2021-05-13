import re

lis_auto = []
lis_opt = []

flag = True

with open('./fmnist_param3_4/log.txt') as f:
    lis = f.readlines()
    count = 0
    for l in lis:
        pattern1 = re.compile(r'Test AUC: \d+.(\d+)')
        res1 = pattern1.search(l)
        if res1 :
            if flag:
                flag = not flag
                lis_auto.append(float(res1.group(0).split(' ')[-1]))
            else:
                flag = not flag
                lis_opt.append(float(res1.group(0).split(' ')[-1]))
print(lis_auto)
print(lis_opt)
print(len(lis_opt))
