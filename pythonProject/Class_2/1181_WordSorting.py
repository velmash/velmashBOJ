from functools import cmp_to_key

def compare_items(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    else:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

n = int(input())

wordsSet = set()
for i in range(n):
    wordsSet.add(input())

result = sorted(wordsSet, key=cmp_to_key(compare_items))

for r in result:
    print(r)