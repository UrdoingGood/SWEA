import sys
sys.stdin = open("input.txt", "r")

def dfs(arr, cx, cy):
    visited = [[False]*N for _ in range(N)] # 방문한 곳 표시
    res = 0 # 최대 길이 저장할 변수
    dxy = [(1,0),(0,1),(-1,0),(0,-1)]

    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy

        # 범위 넘어가는지 확인
        if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
            return res

        # 다음 높이가 같거나 더 높으면, 현재보다 낮아질때까지 K번 내로 1씩 깎아내기
        if arr[cx][cy] <= arr[nx][ny]:
            for _ in range(K):
                if arr[cx][cy] > arr[nx][ny]:
                    break
                arr[nx][ny] -= 1

        visited[cx][cy] = True  # 현재 위치 방문 체크
        res += 1 # 방문 했으므로 길이 하나 추가
        dfs(arr, nx, ny)

    return res

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)] # 산


    # 가장 높은 높이 찾기
    max_point = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > max_point:
                max_point = mountain[i][j]

    # 가장 높은 봉우리라면 스타트
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_point:
                result = dfs(mountain, i, j)

    print(f'#{test_case} {result}')