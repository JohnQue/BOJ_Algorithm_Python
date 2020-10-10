from collections import deque

def solution(n, customers):
    answer = 0
    kiosk = [[0, 0] for _ in range(n)]

    q = deque()
    q.append(customers[0])

    while q:
        tmp = q.popleft()

        # 현재 고객 방문시간 정보를 이용해 키오스크들 정보 갱신
        # 미사용중이면 미사용시간 늘려주고, 사용중이면 사용 끝났는지 아직인지

        # 미사용중인 키오스크 중 가장 앞에 있는 키오스크 가져오기
        if kiosk:
            now = kiosk.pop(0)
            q.append()
        else:
            q.append(tmp)
        # 해당 고객은 그 키오스크 이용
        # 만약 사용가능한 키오스크가 없다 => 키오스크가 empty
        # 그럼 큐에 다시 집어넣고 cnt++안해주고 돌리자

    return answer


# result = 4
print(solution(3, ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]))
# result = 2
print(solution(2, ["02/28 23:59:00 03","03/01 00:00:00 02", "03/01 00:05:00 01"]))
