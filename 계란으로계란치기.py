def dfs(idx, cnt):
    global res, n
    if idx == n or cnt == n-1:
        res = max(res, cnt)
        return
    if eggs[idx][0] <= 0:
        dfs(idx+1, cnt)
        return
    for i in range(n):
        tmp = cnt
        if i == idx:
            continue
        if eggs[i][0] <= 0:
            continue
        eggs[i][0] -= eggs[idx][1]
        eggs[idx][0] -= eggs[i][1]
        if eggs[i][0] <= 0:
            tmp += 1
        if eggs[idx][0] <= 0:
            tmp += 1
        dfs(idx+1, tmp)
        eggs[i][0] += eggs[idx][1]
        eggs[idx][0] += eggs[i][1]


n = int(input())
res = 0
eggs = [list(map(int, input().split())) for _ in range(n)]
dfs(0, 0)
print(res)