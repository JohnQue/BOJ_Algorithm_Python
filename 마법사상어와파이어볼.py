from collections import deque
dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
n, m, k = map(int, input().split())
q = deque()
for _ in range(m):
    n1, n2, n3, n4, n5 = map(int, input().split())
    q.append((n1-1, n2-1, n3, n4, n5, 1))

time = 1
while time <= k:
    count = [[0 for _ in range(n)] for _ in range(n)]
    if not q:
        break
    while q:
        if time != q[0][5]:
            time += 1
            break
        x, y, mi, si, di, t = q.popleft()
        nx, ny = (x + dx[di] * si) % n, (y + dy[di] * si) % n
        count[nx][ny] += 1
        q.append((nx, ny, mi, si, di, t+1))
    mass = [[0 for _ in range(n)] for _ in range(n)]
    speed = [[0 for _ in range(n)] for _ in range(n)]
    dr = [[0 for _ in range(n)] for _ in range(n)]
    q2 = deque()
    while q:
        x, y, mi, si, di, t = q.popleft()
        if count[x][y] < 2:
            q2.append((x, y, mi, si, di, t))
            continue
        mass[x][y] += mi
        speed[x][y] += si
        if di % 2:
            # 홀수
            if dr[x][y] == 2:
                # 전에 짝수면 1,3,5,7을 위해 3으로
                dr[x][y] = 3
            elif not dr[x][y]:
                dr[x][y] = 1
        else:
            # 짝수
            if dr[x][y] == 1:
                # 전에 홀수면 1,3,5,7을 위해 3으로
                dr[x][y] = 3
            elif not dr[x][y]:
                dr[x][y] = 2
    for i in range(n):
        for j in range(n):
            if not mass[i][j]:
                continue
            # 질량이 있다 => 4개의 파이어볼로 쪼개져야 한다.
            fireball = mass[i][j] // 5
            new_speed = speed[i][j] // count[i][j]
            if fireball:
                # 방향이 1이나 2면 전부다 짝수 또는 전부다 홀수임을 뜻함 => 0,2,4,6
                if dr[i][j] == 1 or dr[i][j] == 2:
                    for p in [0, 2, 4, 6]:
                        q.append((i, j, fireball, new_speed, p, t))
                # 나머지는 짝,홀수가 섞여있으므로 1,3,5,7
                else:
                    for p in [1, 3, 5, 7]:
                        q.append((i, j, fireball, new_speed, p, t))
    if q2:
        q.extend(q2)
ans = 0
for i in range(len(q)):
    ans += q[i][2]
print(ans)