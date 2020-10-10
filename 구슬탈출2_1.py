from collections import deque
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
dxs, dys = (0, 1, 0, -1), (1, 0, -1, 0)


def bfs(RED, BLUE):
    q = deque()
    q.append((1, RED[0], RED[1], BLUE[0], BLUE[1]))
    while q:
        cnt, rx, ry, bx, by = q.popleft()
        if cnt > 10:
            break
        for dx, dy in zip(dxs, dys):
            r_out, b_out, flag = False, False, False
            nrx, nry = rx, ry
            while True:
                nrx += dx
                nry += dy
                if arr[nrx][nry] == 'O':
                    r_out = True
                    break
                if arr[nrx][nry] == '#':
                    nrx -= dx
                    nry -= dy
                    break
                if [nrx, nry] == [bx, by]:
                    nrx -= dx
                    nry -= dy
                    flag = True
                    break
            nbx, nby = bx, by
            while True:
                nbx += dx
                nby += dy
                if arr[nbx][nby] == 'O':
                    b_out = True
                    break
                if arr[nbx][nby] == '#':
                    nbx -= dx
                    nby -= dy
                    if flag:
                        nrx, nry = nbx - dx, nby - dy
                    break
                if [nbx, nby] == [nrx, nry]:
                    nbx -= dx
                    nby -= dy
                    break
            if b_out or rx == nrx and ry == nry and bx == nbx and by == nby:
                continue
            if r_out:
                print(cnt)
                return
            q.append((cnt+1, nrx, nry, nbx, nby))
    print(-1)


red, blue = [], []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            red = [i, j]
        elif arr[i][j] == 'B':
            blue = [i, j]

bfs(red, blue)