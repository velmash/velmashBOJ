n = int(input())
scoreArr = list(map(int, input().split()))

maxScore = max(scoreArr)

for index, score in enumerate(scoreArr):
    newScore = score/maxScore*100
    scoreArr[index] = newScore

print(sum(scoreArr)/len(scoreArr))