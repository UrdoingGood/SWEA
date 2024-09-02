import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(arr, i, j):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(i, j)])
    visited = [['-'] for _ in range(N)]
    min_dist = 0

    while queue:
        dist = 0
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if arr[i][j] == 'W':
                return min_dist = min(dist, min_dist)

            if 0 <= nx < M and 0 <= ny < N:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    return -1

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    print(f"#{test_case} {}")