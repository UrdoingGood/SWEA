import sys
sys.stdin = open("input.txt", "r")

def rotation(num, chance, count, new_num, max_num):
    if count == chance:
        return max_num
    for i in range(len(num)):
        if num[i] and not
            rotation(num)

T = int(input())
for test_case in range(1, T + 1):
    num, chance = list(input().split()) # 입력 받기
    new_num = ''  # 교환된 결과 저장할 곳
    max_num = 0  # 최댓값 저장할 곳
    count = 0  # 교환 횟수
    rotation(num, chance, count, new_num, max_num)


