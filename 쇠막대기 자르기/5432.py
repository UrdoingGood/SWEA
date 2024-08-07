import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    parentheses = input()
    stack = []
    count = 0
    for p in parentheses:
        if p == '(':
            stack.append(p)
            count += 1
        if p == ')':
            stack.pop()


    print(f"#{test_case}{res}")

