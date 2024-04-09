from collections import deque

def min_operations_to_one(n):
    queue = deque([(n, 0)])  # (현재 숫자, 연산 횟수)
    visited = [False] * (n + 1)  # 방문 체크 배열
    visited[n] = True

    while queue:
        current, count = queue.popleft()

        # 현재 숫자가 1이면 종료
        if current == 1:
            return count

        # 가능한 연산들을 큐에 추가
        if current % 3 == 0 and not visited[current // 3]:
            visited[current // 3] = True
            queue.append((current // 3, count + 1))
        if current % 2 == 0 and not visited[current // 2]:
            visited[current // 2] = True
            queue.append((current // 2, count + 1))
        if current > 1 and not visited[current - 1]:
            visited[current - 1] = True
            queue.append((current - 1, count + 1))

# 입력 받기
n = int(input())
print(min_operations_to_one(n))
