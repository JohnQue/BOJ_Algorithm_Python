from collections import deque
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


# 빨간 구슬 굴리기
# x 세로
# y 가로
# d 방향 (상하좌우 순)
def roll_red(x, y, d):
    nx, ny = x, y
    while True:
        if arr[nx + dx[d]][ny + dy[d]] != '.':
            break
        nx += dx[d]
        ny += dy[d]
    return nx, ny


# 파란 구슬 굴리기 (이하 생략)
def roll_blue(x, y, d):
    nx, ny = x, y
    while True:
        if arr[nx + dx[d]][ny + dy[d]] != '.':
            break
        nx += dx[d]
        ny += dy[d]
    return nx, ny


rx, ry = -1, -1 # 빨간 구슬 좌표
bx, by = -1, -1 # 파란 구슬 좌표

# 구슬 좌표 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            bx, by = i, j
            arr[i][j] = '.'


def bfs(r_x, r_y, b_x, b_y):
    q = deque()
    q.append((0, r_x, r_y, b_x, b_y))

    while q:
        cnt, red_x, red_y, blue_x, blue_y = q.popleft()
        if cnt >= 10:
            break
        for dr in range(4):
            if not dr:
                if red_x < blue_x: # 빨간 구슬 먼저 위로 구름
                    nrx, nry = roll_red(red_x, red_y, dr)
                    arr[nrx][nry] = 'R'
                    nbx, nby = roll_blue(blue_x, blue_y, dr)
                else:
                    nbx, nby = roll_blue(blue_x, blue_y, dr)
                    arr[nbx][nby] = 'B'
                    nrx, nry = roll_red(red_x, red_y, dr)
                arr[nrx][nry], arr[nbx][nby] = '.', '.'
                if arr[nrx-1][nry] == 'O': # 빨간 구슬이 나가는 경우
                    if nry == nby and nrx + 1 == nbx:
                        # 파란 구슬도 빠져나간다면 바로 밑에 있을 것임 => 큐에 삽입하지 않는다.
                        continue
                    else:
                        print(cnt+1)
                        return
                elif arr[nbx-1][nby] == 'O':
                    continue
            elif dr == 1:
                if red_x > blue_x: # 빨간 구슬 먼저 아래로 구름
                    nrx, nry = roll_red(red_x, red_y, dr)
                    arr[nrx][nry] = 'R'
                    nbx, nby = roll_blue(blue_x, blue_y, dr)
                else:
                    nbx, nby = roll_blue(blue_x, blue_y, dr)
                    arr[nbx][nby] = 'B'
                    nrx, nry = roll_red(red_x, red_y, dr)
                arr[nrx][nry], arr[nbx][nby] = '.', '.'
                if arr[nrx+1][nry] == 'O': # 빨간 구슬이 나가는 경우
                    if nry == nby and nrx - 1 == nbx:
                        # 파란 구슬도 빠져나간다면 바로 위에 있을 것임 => 큐에 삽입하지 않는다.
                        continue
                    else:
                        print(cnt+1)
                        return
                elif arr[nbx+1][nby] == 'O':
                    continue
            elif dr == 2:
                if red_y < blue_y: # 빨간 구슬 먼저 좌로 구름
                    nrx, nry = roll_red(red_x, red_y, dr)
                    arr[nrx][nry] = 'R'
                    nbx, nby = roll_blue(blue_x, blue_y, dr)
                else:
                    nbx, nby = roll_blue(blue_x, blue_y, dr)
                    arr[nbx][nby] = 'B'
                    nrx, nry = roll_red(red_x, red_y, dr)
                arr[nrx][nry], arr[nbx][nby] = '.', '.'
                if arr[nrx][nry-1] == 'O': # 빨간 구슬이 나가는 경우
                    if nrx == nbx and nry+1 == nby:
                        # 파란 구슬도 빠져나간다면 바로 오른쪽에 있을 것임 => 큐에 삽입하지 않는다.
                        continue
                    else:
                        print(cnt+1)
                        return
                elif arr[nbx][nby-1] == 'O':
                    continue
            else:
                if red_y > blue_y: # 빨간 구슬 먼저 우로 구름
                    nrx, nry = roll_red(red_x, red_y, dr)
                    arr[nrx][nry] = 'R'
                    nbx, nby = roll_blue(blue_x, blue_y, dr)
                else:
                    nbx, nby = roll_blue(blue_x, blue_y, dr)
                    arr[nbx][nby] = 'B'
                    nrx, nry = roll_red(red_x, red_y, dr)
                arr[nrx][nry], arr[nbx][nby] = '.', '.'
                if arr[nrx][nry+1] == 'O': # 빨간 구슬이 나가는 경우
                    if nrx == nbx and nry-1 == nby:
                        # 파란 구슬도 빠져나간다면 바로 왼쪽에 있을 것임 => 큐에 삽입하지 않는다.
                        continue
                    else:
                        print(cnt+1)
                        return
                elif arr[nbx][nby+1] == 'O':
                    continue
            if red_x == nrx and red_y == nry and blue_x == nbx and blue_y == nby:
                continue
            q.append((cnt+1, nrx, nry, nbx, nby))
    print(-1)


bfs(rx, ry, bx, by)
