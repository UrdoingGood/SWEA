T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    count = 0
    
    for i in range(N):
        if M%2 == 1:
            count += 1
        M = M//2
	
    if count == N:
        status = 'ON'
    else:
        status = 'OFF'
            
    print(f"#{test_case} {status}")

'''
# 런타임 에러난 코드
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    stack = []
    
    if M == 0:
        stack.append(0)
    while M > 0:
        remain = M % 2
        stack.append(remain)
        M = M // 2

    for i in range(N):
        if stack.pop(0) == 1:
            status = 'ON'
        else:
            status = 'OFF'
            break
            
    print(f"#{test_case} {status}")
'''