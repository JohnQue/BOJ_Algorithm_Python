dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)


def dfs(idx, c_cnt, l_cnt):
    global n, arr, cores, mx, mn, total
    if idx == total:
        if c_cnt > mx:
            mx = c_cnt
            mn = l_cnt
        elif c_cnt == mx:
            mn = min(mn, l_cnt)
        return
    if c_cnt + total - idx < mx:
        return
    x, y = cores[idx]
    for d in range(4):
        if possible(x, y, d):
            dfs(idx+1, c_cnt+1, l_cnt+setting(x, y, d, 2))
            setting(x, y, d, 0)
    dfs(idx+1, c_cnt, l_cnt)


def possible(x, y, d):
    global arr, n
    while True:
        x += dx[d]
        y += dy[d]
        if arr[x][y]:
            return False
        if x == 0 or x == n-1 or y == 0 or y == n-1:
            break
    return True


def setting(x, y, d, s):
    global arr, n
    cnt = 0
    while True:
        x += dx[d]
        y += dy[d]
        arr[x][y] = s
        cnt += 1
        if x == 0 or x == n-1 or y == 0 or y == n-1:
            break
    return cnt


tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cores = []
    mx = 0
    mn = 1e9
    total = 0
    for i in range(1, n-1):
        for j in range(1, n-1):
            if arr[i][j]:
                total += 1
                cores.append((i, j))
    dfs(0, 0, 0)
    print("#{} {}".format(t, mn))
