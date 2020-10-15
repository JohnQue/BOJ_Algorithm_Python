from collections import deque

# 1,2,3,4 => 상하좌우
dx, dy = (0, -1, 1, 0, 0), (0, 0, 0, -1, 1)

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
smell = [[0 for _ in range(n)] for _ in range(n)]
curr_dr = [0]+[*map(int, input().split())]
priority = []
for i in range(m):
    priority.append([list(map(int, input().split())) for _ in range(4)])
q = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            q.append([i, j, arr[i][j], curr_dr[arr[i][j]]])
            smell[i][j] = k
time = 0
temp = []
ans = 0
while q:
    # s n번째 상어, dr 상어 방향
    x, y, s, dr = q.popleft()

    # 빈 공간이 있으면 우선순위에 따라 빈 공간으로 이동
    empty = True
    for d in priority[s-1][dr-1]:
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if not arr[nx][ny]:
            find = False
            for z in range(len(temp)):
                if (nx, ny) == (temp[z][0], temp[z][1]):
                    find = True
                    if s < temp[z][2]:
                        temp[z][2] = s
                        temp[z][3] = d
            if not find:
                temp.append([nx, ny, s, d])
            empty = False
            break

    if empty:
        # 빈 공간이 없다면 우선순위에 따라 자기 냄새가 있는 칸으로 이동
        for d in priority[s-1][dr-1]:
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] == s:
                find = False
                for z in range(len(temp)):
                    if (nx, ny) == (temp[z][0], temp[z][1]):
                        find = True
                        if s < temp[z][2]:
                            temp[z][2] = s
                            temp[z][3] = d
                if not find:
                    temp.append([nx, ny, s, d])
                break

    if not q:
        # 시간이 지날때마다 냄새 갱신
        time += 1
        if time > 1000:
            ans = -1
            break

        for i in range(n):
            for j in range(n):
                if smell[i][j]:
                    smell[i][j] -= 1
                    if not smell[i][j]:
                        arr[i][j] = 0

        for fx, fy, fs, fd in temp:
            arr[fx][fy] = fs
            smell[fx][fy] = k
            q.append((fx, fy, fs, fd))
        if len(temp) == 1:
            ans = time
            break
        temp = []
print(ans)
