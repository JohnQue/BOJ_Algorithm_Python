from collections import deque
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
dxs, dys = (-1, 1, 0, 0), (0, 0, -1, 1)
rex, rey = -1, -1 # 빨간 구슬 좌표
blx, bly = -1, -1 # 파란 구슬 좌표

# 구슬 좌표 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            rex, rey = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            blx, bly = i, j
            arr[i][j] = '.'


def bfs(r_x, r_y, b_x, b_y):
    q = deque()
    q.append((1, r_x, r_y, b_x, b_y))

    while q:
        cnt, red_x, red_y, blue_x, blue_y = q.popleft()
        if cnt > 10:
            break
        for dx, dy in zip(dxs, dys):
            b_out, r_out = False, False
            rx, ry = red_x, red_y
            bx, by = blue_x, blue_y
            flag = False
            while True:
                rx += dx
                ry += dy
                if arr[rx][ry] == 'O':
                    r_out = True  # 빨간 구슬 아웃
                    break
                elif arr[rx][ry] == '#':
                    rx -= dx
                    ry -= dy
                    break
                if [rx, ry] == [bx, by]:  # 이 말은 무조건 파란 구슬이 먼저 움직인단 소리
                    flag = True
                    rx -= dx
                    ry -= dy
                    break
            while True:
                bx += dx
                by += dy
                if arr[bx][by] == 'O':  # 기울인 곳에 빨간 구슬은 일단 없음
                    b_out = True  # 파란 구슬 아웃
                    break
                elif arr[bx][by] == '#':
                    bx -= dx
                    by -= dy
                    if flag:
                        rx = bx - dx
                        ry = by - dy
                    break
                if [bx, by] == [rx, ry]:  # 빨간 구슬이 먼저 움직임
                    bx -= dx
                    by -= dy
                    break
            if b_out or [red_x, red_y] == [rx, ry] and [blue_x, blue_y] == [bx, by]:
                continue
            if r_out:
                print(cnt)
                return
            q.append((cnt+1, rx, ry, bx, by))
    print(-1)


bfs(rex, rey, blx, bly)
