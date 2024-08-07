from collections import deque
import sys
sys.stdin = open("input.txt", "r")


def recovery(arr, x, y):
    global min_time
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * N for _ in range(N)]
    taken_time = 0
    time = []
    queue = deque([(x, y)])

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny]:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = True

            taken_time += arr[nx][ny]
            print(arr[nx][ny])
            if (nx, ny) == (N - 1, N - 1): # 도착점
                time.append(taken_time)
                return min(time)
    return 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    min_time = float('inf')

    for i in range(N):
        for j in range(N):
            if (i, j) == (0, 0): # 출발점
                result = recovery(arr, i, j)

    print(f"#{test_case} {result}")