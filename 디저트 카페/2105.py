import sys
sys.stdin = open("input.txt", "r")

def dfs(stores, cx, cy, count, chk_num):
    dxy = [(1,1), (1,-1), (-1,-1), (-1,1)] # 상우, 하우, 하좌, 상좌 => 시계방향 사각형으로 돌도록 함
    chk_num = [] # 방문한 가게의 디저트 숫자를 담아둘 리스트
    global max_count

    visited[cx][cy] = True

    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy

        # 사각형이 가장 크면 되는거니까,
        # 범위 넘어가면 다음 방향으로 틀도록
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        # 처음 위치로 돌아오면 종료
        if (nx, ny) == (cx, cy):
            return max_count

        # 이동 가능한 경우
        visited[nx][ny] = True # 방문 했다고 표시
        if stores[nx][ny] in chk_num: # 만약 같은 숫자의 디저트를 팔고 있으면 못 감
            continue
        chk_num.append(stores[nx][ny]) # 방문한 가게의 디저트 숫자 담기
        dfs(stores, nx, ny, count, chk_num)
        max_count = max(max_count, count)
        visited[nx][ny] = False # 방문 복구

    return max_count


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # N*N 크기 디저트 카페

    visited = [[False]*N for _ in range(N)] # 방문 여부 확인할 리스트
    max_count = 0 # 디저트 최대 종류 수

    for i in range(N):
        for j in range(N):
            result = dfs(arr, i, j, 0, [])

    print(f"#{test_case} {result}")