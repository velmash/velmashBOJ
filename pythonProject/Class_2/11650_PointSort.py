from functools import cmp_to_key

def compare(a, b):
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    else:
        if a[1] < b[1]:
            return -1
        elif a[1] > b[1]:
            return 1
        else:
            return 0

n = int(input())
pointArr = []

for i in range(n):
    x, y = map(int, input().split())
    pointArr.append((x, y))

sortedPointArr = sorted(pointArr, key=cmp_to_key(compare))
for i in sortedPointArr:
    print(i[0], i[1])