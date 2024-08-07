# 재귀
# 자석의 회전방향을 모두 구한 뒤, 이 회전방향에 따라 회전한다. 그리고 점수를 더한다.

import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    K = int(input())
    # 주어진 자석이 4개이므로 4개의 입력값을 받음
    magnet_list = [deque(list(map(int, input().split()))) for _ in range(4)]
    # 회전 정보
    rotate_info_list = [list(map(int, input().split())) for _ in range(K)]
    score_sum = 0 # 획득한 점수의 총 합을 저장할 변수

    # 이 함수를 통해서 각 자석이 어디로 회전해야하는 지를 구할 수 있다
    # visited에 저장된다
    def rotate_magnet(mag, rot, visited):
        if visited[mag] >= 1:
            return

        visited[mag] = 1 if rot == 1 else 2

        # 0번째 자석이라는 것 => index 2랑 비교를 한다(3시 방향에 있는 것)
        if mag == 0:
            # index 6 => 9시를 의미함
            # 서로 극이 다르면, 회전을 해야하므로, 옆의 자석으로 다시 재귀 호출
            if magnet_list[mag][2] != magnet_list[mag + 1][6]:
                rotate_magnet(mag + 1, -rot, visited)

        elif mag == 1 or mag == 2:
            # 오른쪽이랑 비교한다.
            if magnet_list[mag][2]!= magnet_list[mag - 1][6]:
                rotate_magnet(mag + 1, -rot, visited)
            # 왼쪽이랑 비교한다. index = 6 => 9시를 의미함
            if magnet_list[mag][6]!= magnet_list[mag + 1][2]:
                rotate_magnet(mag - 1, -rot, visited)

        elif mag == 3:
            if magnet_list[mag][6] != magnet_list[mag - 1][3]:
                rotate_magnet(mag - 1, -rot, visited)

    # 주어진 회전 정보에 따라서 자석을 회전시켜야 함
    for rotate_info in rotate_info_list:
        # 마그넷 번호, 회전 정보
        # rotate_dif = 1(시계), -1(반시계)
        magnet_num, rotate_dir = rotate_info
        
        # 각 자석이 어떤 방향으로 회전해야하는 지를 저장하는 변수
        # visited[1] = 시계 방향, visited[2] = 반시계 방향
        # 회전을 시켰는지 확인하는 용도
        # 밑에서 로직을 작성해서 visited를 채워갈건데,
        # 로직을 완료한 다음에는 visited를 순회하면서 자석을 회전시킬 것임
        visited = [0] * 4
        
        # 번호에 해당하는 자석이 어떤 방향으로 회전해야 하는지 확인하는 함수
        # 1. 자석 번호를 파라미터로 넘기고
        # 2. 해당 자석이 어느 방향으로 회전할 건지도 넘기고
        # 3. visited로 방무누 여부로 확인하면서 회전 여부도 갱신
        rotate_magnet(magnet_num - 1, rotate_dir, visited)

        # i에는 인덱스, v에는 값
        for i, v in enumerate(visited):
            if v == 1: # 시계 방향, 제일 뒤를 빼서 앞에 넣음
                magnet_list[i].appendleft(magnet_list[i].pop())
                magnet_list[i].rotate(1) # 시계 방향으로 데이터를 회전
            elif v == 2: # 반시게 방향, 제일 앞에서 빼서 뒤에 넣음
                magnet_list[i].append(magnet_list[i].popleft())
                magnet_list[i].rotate(-1) # 반시계 방향으로 데이터를 회전

    # 결과를 계산하자
    # 4개의 자석에 대해 빨간색 화살표 위치 (인덱스 0)인 부분을 확인
    # S극이면 점수를 준다
    score_list = [1,2,4,8]
    for i in range(4):
        if magnet_list[i][0] == 1:
            score_sum += score_list[i]
        
    print(f"#{test_case} {score_sum}")