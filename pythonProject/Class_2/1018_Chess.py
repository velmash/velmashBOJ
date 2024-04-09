def repaint_count(board, start_row, start_col):
    # 체스판 패턴 두 가지
    pattern1 = ['BWBWBWBW', 'WBWBWBWB'] * 4
    pattern2 = ['WBWBWBWB', 'BWBWBWBW'] * 4

    # 첫 번째 패턴에 대한 다시 칠할 칸의 수
    repaint1 = 0
    repaint2 = 0

    for i in range(8):
        for j in range(8):
            if board[start_row + i][start_col + j] != pattern1[i][j]:
                repaint1 += 1
            if board[start_row + i][start_col + j] != pattern2[i][j]:
                repaint2 += 1

    # 두 패턴 중에서 다시 칠할 칸이 더 적은 경우를 반환
    return min(repaint1, repaint2)

def minimum_repaints(n, m, board):
    min_repaint = float('inf')  # 가능한 최소값을 찾기 위해 무한대로 초기화

    # 모든 가능한 8x8 시작 위치에 대해 검사
    for i in range(n - 7):  # n-7과 m-7은 8x8 체스판이 시작할 수 있는 마지막 인덱스
        for j in range(m - 7):
            repaints = repaint_count(board, i, j)
            if repaints < min_repaint:
                min_repaint = repaints

    return min_repaint

# 입력
n, m = map(int, input().split())
board = [input() for _ in range(n)]

# 결과 출력
print(minimum_repaints(n, m, board))
