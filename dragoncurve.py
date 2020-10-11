from collections import deque
from copy import deepcopy

n = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]
dy, dx = (0, -1, 0, 1), (1, 0, -1, 0)
for _ in range(n):
    x, y, d, g = map(int, input().split())

    # 0 세대는 그냥 처리
    arr[y][x] = 1
    if 0 <= y + dy[d] <= 100 and 0 <= x + dx[d] <= 100:
        arr[y + dy[d]][x + dx[d]] = 1
    stack = deque()
    stack.append(d)
    sy, sx = y + dy[d], x + dx[d]
    gen = 0

    # 1세대부터
    while gen < g:
        gen += 1
        tmp = deepcopy(stack) # 매번 드래곤 커브를 위해 만드는 스택 (값을 빼지 않는 스택을 깊은 복사)
        while tmp:
            dr = (tmp.pop() + 1) % 4
            stack.append(dr)
            sy, sx = sy + dy[dr], sx + dx[dr]
            if sx < 0 or sx > 100 or sy < 0 or sy > 100:
                continue
            arr[sy][sx] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i][j+1] and arr[i+1][j] and arr[i+1][j+1]:
            answer += 1
print(answer)
