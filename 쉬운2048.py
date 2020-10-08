n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]


def convert(a):
    tmp = [i for i in a if i]
    for i in range(1, len(tmp)):
        if tmp[i] == tmp[i-1]:
            tmp[i-1] *= 2
            tmp[i] = 0
    new_tmp = [i for i in tmp if i]
    return new_tmp + [0] * (n-len(new_tmp))


def rotate(x):
    return [[x[i][j] for i in range(n-1, -1, -1)] for j in range(n)]


def dfs(cnt, arr):
    max_value = max([max(i) for i in arr])
    if cnt == 5:
        return max_value
    for _ in range(4):
        x = [convert(arr[i]) for i in range(n)]
        if x != arr:
            max_value = max(max_value, dfs(cnt+1, x))
        arr = rotate(arr)
    return max_value


print(dfs(0, MAP))