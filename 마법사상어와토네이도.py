from collections import deque
dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

sx, sy = n // 2, n // 2
out = 0
q = deque()
q.append((sx, sy, 1, 0, 0, 0))
while q:
    x, y, line, lcnt, cnt, d = q.popleft()
    if not x and not y:
        break
    x, y = x + dx[d], y + dy[d]
    total = 0

    # 모든 것은 왼쪽기준
    # 위아래 한칸
    nx, ny = x + dx[(d+1) % 4], y + dy[(d+1) % 4]
    sand = (arr[x][y] * 7) // 100
    if 0 <= nx < n and 0 <= ny < n:
        arr[nx][ny] += sand
    else:
        out += sand
    total += sand

    nx, ny = x + dx[(d+3) % 4], y + dy[(d+3) % 4]
    sand = (arr[x][y] * 7) // 100
    if 0 <= nx < n and 0 <= ny < n:
        arr[nx][ny] += sand
    else:
        out += sand
    total += sand

    # 위아래 두칸
    nx, ny = x + dx[(d + 1) % 4] * 2, y + dy[(d + 1) % 4] * 2
    sand = (arr[x][y] * 2) // 100
    if 0 <= nx < n and 0 <= ny < n:
        arr[nx][ny] += sand
    else:
        out += sand
    total += sand

    nx, ny = x + dx[(d + 3) % 4] * 2, y + dy[(d + 3) % 4] * 2
    sand = (arr[x][y] * 2) // 100
    if 0 <= nx < n and 0 <= ny < n:
        arr[nx][ny] += sand
    else:
        out += sand
    total += sand

    # 오른쪽 대각선 두칸
    nx, ny = x + dx[(d+1) % 4], y + dy[(d+1) % 4]
    nx, ny = nx - dx[d], ny - dy[d]
    sand = arr[x][y] // 100
    if 0 <= nx < n and 0 <= ny < n:
        arr[nx][ny] += sand
    else:
        out += sand
    total += sand

    nx, ny = x + dx[(d+3) % 4], y + dy[(d+3) % 4]
    nx, ny = nx - dx[d], ny - dy[d]
    sand = arr[x][y] // 100
    if 0 <= nx < n and 0 <= ny < n:
        arr[nx][ny] += sand
    else:
        out += sand
    total += sand

    # 왼쪽 대각선 두칸
    nx, ny = x + dx[(d+1) % 4], y + dy[(d+1) % 4]
    nx, ny = nx + dx[d], ny + dy[d]
    sand = (arr[x][y] * 10) // 100
    if 0 <= nx < n and 0 <= ny < n:
        arr[nx][ny] += sand
    else:
        out += sand
    total += sand

    nx, ny = x + dx[(d+3) % 4], y + dy[(d+3) % 4]
    nx, ny = nx + dx[d], ny + dy[d]
    sand = (arr[x][y] * 10) // 100
    if 0 <= nx < n and 0 <= ny < n:
        arr[nx][ny] += sand
    else:
        out += sand
    total += sand

    # 왼쪽에서 두칸
    nx, ny = x + dx[d] * 2, y + dy[d] * 2
    sand = (arr[x][y] * 5) // 100
    if 0 <= nx < n and 0 <= ny < n:
        arr[nx][ny] += sand
    else:
        out += sand
    total += sand

    # 마지막 왼쪽에서 한칸
    sand = arr[x][y] - total
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < n and 0 <= ny < n:
        arr[nx][ny] += sand
    else:
        out += sand

    lcnt += 1
    if lcnt == line:
        cnt += 1
        lcnt = 0
        d = (d + 1) % 4

    if cnt == 2:
        if x:
            line += 1
        cnt = 0

    q.append((x, y, line, lcnt, cnt, d))
print(out)