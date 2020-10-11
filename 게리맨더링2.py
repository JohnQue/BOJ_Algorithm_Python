n = int(input())

arr = [[*map(int, input().split())] for _ in range(n)]
min_value = 987654321
dx, dy = (-1, 1, 1, -1), (1, 1, -1, -1)
for x in range(1, n-1):
    for y in range(n-2):
        for d1 in range(1, n - 1):
            for d2 in range(1, n - 1):
                tmp = [[0 for _ in range(n)] for _ in range(n)]
                sx, sy = x, y
                tmp[sx][sy] = 5
                out = False
                for i in range(d1):
                    sx, sy = sx + dx[0], sy + dy[0]
                    if sx < 0 or sx >= n or sy < 0 or sy >= n:
                        out = True
                        break
                    tmp[sx][sy] = 5
                x1, y1 = sx, sy
                if out:
                    continue
                for i in range(d2):
                    sx, sy = sx + dx[1], sy + dy[1]
                    if sx < 0 or sx >= n or sy < 0 or sy >= n:
                        out = True
                        break
                    tmp[sx][sy] = 5
                if out:
                    continue
                x2, y2 = sx, sy
                for i in range(d1):
                    sx, sy = sx + dx[2], sy + dy[2]
                    if sx < 0 or sx >= n or sy < 0 or sy >= n:
                        out = True
                        break
                    tmp[sx][sy] = 5
                if out:
                    continue
                x3, y3 = sx, sy
                for i in range(d2):
                    sx, sy = sx + dx[3], sy + dy[3]
                    if sx < 0 or sx >= n or sy < 0 or sy >= n:
                        out = True
                        break
                    tmp[sx][sy] = 5
                if out:
                    continue
                x4, y4 = sx, sy

                for i in range(x):
                    for j in range(y1+1):
                        if tmp[i][j] == 5:
                            break
                        tmp[i][j] = 1
                for i in range(x, n):
                    for j in range(y3):
                        if tmp[i][j] == 5:
                            break
                        tmp[i][j] = 3

                for i in range(x2+1):
                    if i < x1:
                        for j in range(y1+1, n):
                            tmp[i][j] = 2
                    else:
                        for j in range(y1+i-x1+1, n):
                            tmp[i][j] = 2

                for i in range(x2+1, n):
                    if i <= x3:
                        for j in range(y2-i+x2+1, n):
                            tmp[i][j] = 4
                    else:
                        for j in range(y3, n):
                            tmp[i][j] = 4

                for i in range(n):
                    for j in range(n):
                        if not tmp[i][j]:
                            tmp[i][j] = 5

                total = [0] * 5
                for i in range(n):
                    for j in range(n):
                        total[tmp[i][j]-1] += arr[i][j]
                min_value = min(min_value, max(total)-min(total))

print(min_value)
