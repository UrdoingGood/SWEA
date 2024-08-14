import sys
sys.stdin = open("input.txt", "r")

def dfs(arr, cx, cy, res, chk):
    visited = [[False]*N for _ in range(N)] # 방문한 곳 표시
    dxy = [(1,0),(0,1),(-1,0),(0,-1)]
    global max_res
    count = 0 # 몇 번 깎았는지 체크할 변수

    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy

        tmp_x, tmp_y = nx, ny  # 깎인(깎일 수 있는) 곳을 체크할 변수

        # 범위 넘어가는지 확인
        if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
            continue

        # 깎은 적이 없고, 다음 높이가 같거나 더 높으면,
        # 현재보다 낮아질때까지 K번 내로 1씩 깎아내기
        # 한 번만 깎을 수 있으므로 깎았는지 여부도 체크
        if chk == False and arr[cx][cy] <= arr[nx][ny]:
            for _ in range(K):
                if arr[cx][cy] > arr[nx][ny]:
                    break
                arr[nx][ny] -= 1
                count += 1
                chk = True

        # 깎았는데도 여전히 높이가 같거나 높으면 더이상 갈 수 없으므로 길이 반환
        if chk == True and arr[cx][cy] <= arr[nx][ny]:
            return max_res

        visited[cx][cy] = True  # 현재 위치 방문 체크
        res += 1
        dfs(arr, nx, ny, res, chk)
        max_res = max(max_res, res) # 최대 길이 찾기
        visited[tmp_x][tmp_y] += count # 깎인 곳 원상 복구

    return max_res

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)] # 산
    max_res = 0 # 최대 길이 저장할 변수

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
                result = dfs(mountain, i, j, 0, False)

    print(f'#{test_case} {result}')