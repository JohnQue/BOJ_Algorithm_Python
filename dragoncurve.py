from copy import deepcopy
arr = [[0 for _ in range(101)] for _ in range(101)]
n = int(input())
dy, dx = (0, -1, 0, 1), (1, 0, -1, 0)

# 가로가 먼저 주어짐
for _ in range(n):
    x, y, d, g = map(int, input().split())

    gen = 1
    arr[y][x] = 1
    if 0 <= y+dy[d] <= 100 and 0 <= x+dx[d] <= 100:
        arr[y+dy[d]][x+dx[d]] = 1
    std = (y+dy[d], x+dx[d])
    stack = [(d+1) % 4]

    while gen <= g:
        tmp = deepcopy(stack)
        while tmp:
            dr = tmp.pop()
            ny, nx = std[0]+dy[dr], std[1]+dx[dr]
            stack.append((dr+1) % 4)
            std = (ny, nx)
            if ny < 0 or ny > 100 or nx < 0 or nx > 100:
                continue
            arr[ny][nx] = 1
        gen += 1
answer = 0

for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            answer += 1

print(answer)
