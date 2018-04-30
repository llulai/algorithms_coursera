# Uses python3
n = int(input())
a = [int(x) for x in input().split()]

max_ , sec_max = 0, 0

for el in a:
    if el >= max_:
        sec_max, max_ = max_, el
    elif el > sec_max:
    	sec_max = el

print(sec_max * max_)
