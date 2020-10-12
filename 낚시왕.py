import sys

dx, dy = (0, -1, 1, 0, 0), (0, 0, 0, 1, -1)
# r 세로, c 가로, m 상어 수
r, c, m = map(int, input().split())
arr = [[[] for _ in range(c)] for _ in range(r)]

for _ in range(m):
    # x, y 는 상어 위치, s 속력, d 방향, z 크기
    x, y, s, d, z = map(int, sys.stdin.readline().split())
    arr[x-1][y-1] = [s, d, z]

stage = 0
get = 0
while stage < c:
    # 상어 잡기
    for i in range(r):
        if arr[i][stage]:
            get += arr[i][stage][2]
            arr[i][stage] = []
            break

    # 상어 움직이기
    carr = [[[] for _ in range(c)] for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if arr[x][y]:
                s, d, z = arr[x][y]
                nx, ny, ns = x, y, s
                if d == 1:
                    if nx >= ns:
                        nx += dx[d] * ns
                    else:
                        ns -= nx
                        a = ns % (r-1)
                        ns //= (r-1)
                        if ns % 2:
                            d = 1
                            nx = r-1
                        else:
                            d = 2
                            nx = 0
                        nx += dx[d] * a
                elif d == 2:
                    if r-1-nx >= ns:
                        nx += dx[d] * ns
                    else:
                        ns -= (r-1-nx)
                        a = ns % (r-1)
                        ns //= (r-1)
                        if ns % 2:
                            d = 2
                            nx = 0
                        else:
                            d = 1
                            nx = r-1
                        nx += dx[d] * a
                elif d == 3:
                    if c-1-ny >= ns:
                        ny += dy[d] * ns
                    else:
                        ns -= (c-1-ny)
                        a = ns % (c-1)
                        ns //= (c-1)
                        if ns % 2:
                            d = 3
                            ny = 0
                        else:
                            d = 4
                            ny = c-1
                        ny += dy[d] * a
                else:
                    if ny >= ns:
                        ny += dy[d] * ns
                    else:
                        ns -= ny
                        a = ns % (c-1)
                        ns //= (c-1)
                        if ns % 2:
                            d = 4
                            ny = c-1
                        else:
                            d = 3
                            ny = 0
                        ny += dy[d] * a
                if carr[nx][ny]:
                    if carr[nx][ny][2] < z:
                        carr[nx][ny] = [s, d, z]
                else:
                    carr[nx][ny] = [s, d, z]

    arr = carr
    stage += 1

print(get)