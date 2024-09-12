import sys
sys.stdin = open('input.txt', 'r')


def bfs(si, sj, ei, ej):
    global time
    queue = []

    queue.append((si, sj))
    board_arr[si][sj] = board_arr[ei][ej] = 1

    while queue:
        ci, cj = queue.pop(0)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = ci + dx, cj + dy
            queue.append((ni, nj))

            if board_arr[ni][nj] == 2: # 자신의 몸과 만나면 종료
                return

            if 0 <= ni < N and 0 <= nj < N:
                if board_arr[ni][nj] == 1: # 사과 먹기
                    board_arr[ni][nj] = 0
                else:
                    ei, ej = ei

            # === 수정할 내용
            # 사과 먹으면 뱀 길이 +1
            # time은 이동할때마다 +1
            # 상하/좌우 이동 방향 체크해서 L(왼), D(오) 회전하기

time = 0 # 게임 소요 시간
N = int(input()) # 보드의 크기
board_arr = [[0] * N for _ in range(N)] # 아무것도 없음 : 0 / 사과 : 1 / 뱀 : 2

K = int(input()) # 사과의 개수
for k in range(K): # 사과 심기
    row, col = map(int, input().split())
    board_arr[row][col] = 1

L = int(input()) # 방향 변환 횟수
rotate_arr = [list(map(int, input().split())) for _ in range(L)] # rotate_arr[i][0] : X초 / rotate_arr[i][1] == 'L' : 왼 / rotate_arr[i][1] == 'D' : 오

bfs(0, 1, 0, 0)
print(time)