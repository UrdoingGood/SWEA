import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(input().split()) for _ in range(N)] # 산
    visited = [[False]*N for _ in range(N)] # 방문한 곳 표시
    res = 0 # 최대 길이 저장할 변수


    print(f'#{test_case} {res}')