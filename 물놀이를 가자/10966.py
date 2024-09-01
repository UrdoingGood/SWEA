import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def bfs(arr, N, M):


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]


    print(f"#{test_case} {res}")