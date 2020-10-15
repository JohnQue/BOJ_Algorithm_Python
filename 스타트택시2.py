from collections import deque
import heapq

# BFS용 방향 벡터
dxs, dys = (-1, 0, 0, 1), (0, -1, 1, 0)
n, m, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# stp = start point 손님 위치 모음 리스트
# dsp = destination point 목적지 위치 모음 리스트
stp, dsp = [], []

# sx, sy 운전 시작위치 1부터 시작하므로 1을 빼주면 0부터 시작함 (배열범위 안바꿔도 됨)
sx, sy = map(int, input().split())
sx, sy = sx-1, sy-1

for _ in range(m):
    stx, sty, dsx, dsy = map(int, input().split())
    # 마찬가지로 얘네도 1씩 빼줌
    stx, sty, dsx, dsy = stx-1, sty-1, dsx-1, dsy-1
    stp.append((stx, sty))
    dsp.append((dsx, dsy))

    # 손님 위치만 2로 => 목적지는 안해도 된다. 이유는 이따 알게됨
    arr[stx][sty] = 2

# 이 문제를 풀기 위해선 총 두 개의 BFS가 필요함
# 첫번째로는 시작점에서 손님을 태우러갈때 까지의 BFS
# 두번째로는 손님을 태운 지점부터 목적지까지 갈때의 BFS
# 첫번째의 경우는 heap이 필요하기 때문에 둘은 다르게 구현해줘야 함


# 실제로 손님을 태우고 목적지에 도달한 경우 finished는 1씩 증가되고 m번을 완료하면
# 모든 손님을 태우고 목적지에 데려다준 것이므로 프로그램 종료
# 즉 종료 조건은 두가지인데, 연료를 다 쓸때까지 손님을 다 못 데려다 준 경우가 첫번째고
# 우선 시작점의 위치를 담아 너비우선탐색 실시
# 모든 손님을 태우고 목적지에 데려다준 것이 두번째다.

finished = 0
while finished < m: # m번 완료시 프로그램 종료
    q = deque()
    # x, y좌표와 사용한 연료의 양을 담는다. 이 연료가 현재의 연료보다 많을 경우 프로그램은 종료되야 한다.
    q.append((sx, sy, 0))
    v = [[False for _ in range(n)] for _ in range(n)] # 중복방문을 없애기 위해 visit배열을 만듦
    ff = 987654321 # 가장 가까운 위치의 손님까지 도달하는데 필요한 연료량 저장
    heap = [] # heap에 사용할 리스트
    while q:
        x, y, f = q.popleft()
        # 필요한 연료량을 전부 다 쓰게 될경우는 프로그램을 종료해줘야 한다.
        if f > fuel:
            fuel = -1
            break
        # 가장 가까운 손님보다 더 연료가 필요한 곳은 어차피 지금 갈 필요가 없으므로 스킵
        if ff < f:
            continue
        # 만약 손님이 있는 위치라면 arr[nx][ny]는 2일 것
        if arr[x][y] == 2:
            ff = f # 가장 가까운 위치의 손님을 찾았으므로 필요한 연료량 저장
            # 택시 출발지점과 손님과의 거리가 같은 경우가 여러가지인 경우가 있음
            # 이때는 우선순위를 위해 힙을 사용한다. (x, y 둘다 작은 순이 가장 앞에 온다.)
            heapq.heappush(heap, (x, y, f))
            continue
        # 전부 해당되지 않는 좌표들은 그냥 BFS 계속 진행
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] == 1 or v[nx][ny]:
                # 범위를 벗어났거나, arr[][]값이 1인 경우는 벽이기 때문에, v[][]=True 면 이미 방문했기에 스킵
                continue
            v[nx][ny] = True
            # 범위를 벗어나지 않았다면 BFS를 위해 q에 집어넣는다.
            # 사용한 연료가 1 늘어나므로 +1 해준다.
            q.append((nx, ny, f+1))

    # 전부 큐를 돌고 벗어나면, 이제 heap안에는 택시의 시작점으로부터 가장 가까운 거리에 있는 손님들이 들어있음
    # 그런데 만약 heap이 비어있다면, 그것은 어떤 문제가 생겼음을 의미함 (연료가 다 떨어졌다거나)
    # 고로 프로그램 종료
    if not heap:
        fuel = -1
        break

    # 이제는 첫번째 손님을 태울 차례
    # mx, my는 최단거리에 있는 손님중 가장 왼쪽, 그리고 가장 왼쪽 위의 손님의 좌표
    # mf는 택시 출발지점부터 mx, my까지의 도달할때 필요한 연료량
    mx, my, mf = heapq.heappop(heap)

    # 이동한 만큼의 연료를 빼준다 => 당연히 연료량이 0 이하인지 체크해줘야함
    fuel -= mf

    # 잔여량이 0보다 작거나 같다면 더이상 진행불가하므로 프로그램 종료
    if fuel <= 0:
        fuel = -1
        break

    # 이제 진짜 손님을 태울 연료량도 충분하다고 판단되었으니 손님을 태움
    # 손님을 태웠으므로 2였던 값을 0으로 비워줌
    arr[mx][my] = 0

    # 손님을 태운 mx, my 부분을 또 택시 시작점으로 잡고 목적지까지 가야하므로 큐를 새로 초기화
    q = deque()
    q.append((mx, my, 0))

    # 이게 진짜 중요한 부분인데, 손님을 태운 지점을 이용해 목적지의 좌표를 구할 수 있음
    idx = stp.index((mx, my)) # stp 배열에서 현재 손님 좌표를 가지는 index 리턴
    stp.pop(idx) # 먼저 손님을 태운 점 좌표부터 빼준다.
    px, py = dsp.pop(idx) # 그 idx를 고대로 이용해 목적지 배열에서 빼주면 목적지 좌표가 나온다.
    # 왜냐하면, 우리가 애초에 stp, dsp 배열을 만들때 한줄에 출발지점, 도착지점 좌표를 받아 넣어줬기 때문에 인덱스가 같다.

    v = [[False for _ in range(n)] for _ in range(n)]  # 중복방문을 없애기 위해 visit배열을 만듦

    # 이제 목적지로 가는 BFS 시작
    while q:
        x, y, f = q.popleft()
        # 필요한 연료량을 목적지 도달전에 전부 다 쓰게될 경우는 프로그램을 종료해줘야 한다.
        if f > fuel:
            fuel = -1
            break
        # x와 px, 그리고 y와 py가 같다는 건, 현재 택시가 목적지에 도달했음을 의미한다.
        if x == px and y == py:
            # 따라서 손님을 태운 시점부터 목적지 까지의 연료량을 더해준다 (쓴만큼의 두배를 채워주니 애초에 쓴 양을 더하면 됨)
            fuel += f
            sx, sy = px, py # 시작 지점을 다시 여기로 맞추고 while문을 벗어나 다음 손님을 태운다.
            break
        # 아직 도착지점에 도달하지 못했다면 BFS 실시
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] == 1 or v[nx][ny]:
                continue
            v[nx][ny] = True
            q.append((nx, ny, f+1))
    # 만약 연료량이 0 이하면 더이상 진행 불가이므로 종료
    if fuel <= 0:
        fuel = -1
        break
    finished += 1 # 여기까지 왔다면 성공적으로 목적지에 도달했단 뜻이므로 잘 데려다 준 사람을 +1 해줌
print(fuel) # 반복문을 마치고 최종 남은 연료량 출력 => 갈 수 없으면 break에 의해 지정된 -1 출력
