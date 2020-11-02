tc = int(input())
dx, dy = (0, 0, 1, 0, -1), (0, -1, 0, 1, 0)

for t in range(1, tc+1):
    m, a = map(int, input().split())
    user_a = list(map(int, input().split()))
    user_b = list(map(int, input().split()))
    ax, ay = 1, 1
    bx, by = 10, 10
    bc = [list(map(int, input().split())) for _ in range(a)]
    time = 0
    total = 0

    while time <= m:
        ta, tb = 0, 0
        abc, bbc = 0, 0
        for i, (x, y, c, p) in enumerate(bc):
            if abs(ax - x) + abs(ay - y) <= c:
                if ta < p:
                    ta = p
                    abc = i+1
            if abs(bx - x) + abs(by - y) <= c:
                if tb < p:
                    tb = p
                    bbc = i+1

        if abc != bbc:
            total = total + ta + tb

        else:
            ta, tb = 0, 0
            abc, bbc = 0, 0
            for i, (x, y, c, p) in enumerate(bc):
                if abs(ax - x) + abs(ay - y) <= c:
                    if ta < p:
                        ta = p
                        abc = i+1
            for i, (x, y, c, p) in enumerate(bc):
                if abs(bx - x) + abs(by - y) <= c:
                    if abc != i+1 and tb < p:
                        tb = p
                        bbc = i+1
            tmp = ta + tb
            ta, tb = 0, 0
            abc, bbc = 0, 0
            for i, (x, y, c, p) in enumerate(bc):
                if abs(bx - x) + abs(by - y) <= c:
                    if tb < p:
                        tb = p
                        bbc = i+1
            for i, (x, y, c, p) in enumerate(bc):
                if abs(ax - x) + abs(ay - y) <= c:
                    if bbc != i+1 and ta < p:
                        ta = p
                        abc = i+1
            tmp2 = ta + tb
            total += max(tmp, tmp2)
        if time == m:
            break
        ax += dx[user_a[time]]
        ay += dy[user_a[time]]
        bx += dx[user_b[time]]
        by += dy[user_b[time]]
        time += 1
    print("#{} {}".format(t, total))