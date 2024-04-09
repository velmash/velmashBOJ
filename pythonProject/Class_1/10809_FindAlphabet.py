inputStr = input()

resultArr = [-1] * 26

for index, char in enumerate(inputStr):
    arrIndex = ord(char) - 97
    if resultArr[arrIndex] == -1:
        resultArr[arrIndex] = index

for i in resultArr:
    print(i, end=" ")