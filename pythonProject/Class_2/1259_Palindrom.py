target = ""

while target != 0:
    inputStr = input()

    if int(inputStr) == 0:
        target = 0
        break
    else:
        targetStr = str(inputStr)
        lStr = ""
        rStr = ""

        if len(targetStr) % 2 == 0:
            centerPointL = int(len(targetStr) / 2 - 1)
            centerPointR = int(len(targetStr) / 2)

            lStr = targetStr[:centerPointL + 1]
            tempRStr = targetStr[centerPointL + 1:]
            rStr = tempRStr[::-1]

        else:
            centerPoint = int(len(targetStr) / 2)
            lStr = targetStr[:centerPoint]
            tempRStr = targetStr[centerPoint + 1:]
            rStr = tempRStr[::-1]

        if lStr == rStr:
            print("yes")
        else:
            print("no")

