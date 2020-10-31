from copy import deepcopy
from collections import deque
dx, dy = (-1, 0, 1, 0), (0, -1, 0, 1)


def bfs(bx, by):
    global m
    dq = deque()
    count = 0
    dq.append((bx, by))
    v[bx][by] = True
    while dq:
        qx, qy = dq.popleft()
        count += 1
        for dr in range(4):
            nnx, nny = qx + dx[dr], qy + dy[dr]
            if nnx < 0 or nnx >= m or nny < 0 or nny >= m or v[nnx][nny] or not arr[nnx][nny]:
                continue
            v[nnx][nny] = True
            dq.append((nnx, nny))
    return count


def rotate(si, ei, sj, ej):
    global m, arr
    return [[arr[i][j] for i in range(ei-1, si-1, -1)] for j in range(sj, ej)]


n, q = map(int, input().split())
m = 2 ** n
arr = [list(map(int, input().split())) for _ in range(m)]
level = list(map(int, input().split()))

for l in level:
    l += 1
    if l > n:
        arr = rotate(0, m, 0, m)
    elif l > 0:
        carr = [[0 for _ in range(m)] for _ in range(m)]
        for i in range(0, m, 2 ** l):
            for j in range(0, m, 2 ** l):
                arr1 = rotate(i, i+2 ** (l-1), j, j+2 ** (l-1))
                arr2 = rotate(i, i+2 ** (l-1), j+2 ** (l-1), j+2 ** l)
                arr3 = rotate(i+2 ** (l-1), i+2 ** l, j, j+2 ** (l-1))
                arr4 = rotate(i+2 ** (l-1), i+2 ** l, j+2 ** (l-1), j+2 ** l)
                for a in range(i, i+2 ** (l-1)):
                    for b in range(j, j+2 ** (l-1)):
                        carr[a][b] = arr1[a-i][b-j]
                    for b in range(j+2 ** (l-1), j+2 ** l):
                        carr[a][b] = arr2[a-i][b-(j+2 ** (l-1))]

                for a in range(i+2 ** (l-1), i+2 ** l):
                    for b in range(j, j+2 ** (l-1)):
                        carr[a][b] = arr3[a-(i+2 ** (l-1))][b-j]
                    for b in range(j+2 ** (l-1), j+2 ** l):
                        carr[a][b] = arr4[a-(i+2 ** (l-1))][b-(j+2 ** (l-1))]
        arr = deepcopy(carr)
    # 여까지 하면 이제 돌아간 얼음의 상태가 나옴 => 인접한 곳에 얼음 셋이 없으면 -1 떨굼
    carr = deepcopy(arr)
    for x in range(m):
        for y in range(m):
            if carr[x][y] > 0:
                cnt = 0
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if nx < 0 or nx >= m or ny < 0 or ny >= m or not arr[nx][ny]:
                        continue
                    cnt += 1
                if cnt < 3:
                    carr[x][y] -= 1
    arr = deepcopy(carr)

total = sum(sum(arr[i]) for i in range(m))
v = [[False for _ in range(m)] for _ in range(m)]
max_value = 0
for x in range(m):
    for y in range(m):
        if not v[x][y] and arr[x][y]:
            max_value = max(max_value, bfs(x, y))

print(total, max_value)