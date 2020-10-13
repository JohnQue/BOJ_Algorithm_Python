from collections import deque
import heapq
dxs, dys = (-1, 0, 0, 1), (0, -1, 1, 0)
n, m, f = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

#승객 위치
psg = []
#목적지 위치
des = []

sx, sy = map(int, input().split())
sx, sy = sx-1, sy-1
cnt = 2

for _ in range(m):
    p1, p2, d1, d2 = [*map(int, input().split())]
    p1, p2, d1, d2 = p1-1, p2-1, d1-1, d2-1
    psg.append((p1, p2))
    des.append((d1, d2))
    arr[p1][p2] = 2

finished = 0
while finished < m:
    q = deque()
    q.append((sx, sy, f))
    v = [[False for _ in range(n)] for _ in range(n)]
    heap = []
    foundFuel = 0
    while q:
        x, y, fuel = q.popleft()
        if fuel < 0:
            f = -1
            break
        if foundFuel > fuel:
            break
        if arr[x][y] == 2:
            foundFuel = fuel
            heapq.heappush(heap, (x, y, fuel))
            continue
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] == 1 or v[nx][ny]:
                continue
            v[nx][ny] = True
            q.append((nx, ny, fuel-1))
        if not q:
            f = -1
    if not heap:
        f = -1
        break
    hx, hy, hf = heapq.heappop(heap)
    f -= (f - hf)
    if f <= 0:
        f = -1
        break
    arr[hx][hy] = 0
    q = deque()
    idx = psg.index((hx, hy))
    psg.pop(idx)
    px, py = des.pop(idx)
    q.append((hx, hy, f))
    v = [[False for _ in range(n)] for _ in range(n)]

    while q:
        x2, y2, fuel2 = q.popleft()
        if fuel2 < 0:
            f = -1
            break
        if x2 == px and y2 == py:
            f += (f - fuel2)
            sx, sy = x2, y2
            break
        for dx, dy in zip(dxs, dys):
            nx, ny = x2 + dx, y2 + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] == 1 or v[nx][ny]:
                continue
            v[nx][ny] = True
            q.append((nx, ny, fuel2-1))
        if not q:
            f = -1
    if f <= 0:
        f = -1
        break
    finished += 1
print(f)
