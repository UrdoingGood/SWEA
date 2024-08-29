import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
for n in range(N):
    T, P = map(int, input().split())

    # 남은 일자보다 T가 크면 상담할 수 없음
    if N - n + 1 > T:
        continue

    if