from collections import deque


def solution(depar, hub, dest, roads):
    answer = 0
    obj = {}

    for r in roads:
        if obj.get(r[0]):
            obj[r[0]].append(r[1])
        elif obj.get(r[0]) is None:
            obj[r[0]] = [r[1]]

    q = deque()
    q.append((depar, False)) # 허브를 지나면 False가 True로 변함

    while q:
        city, is_hub = q.popleft()
        if city == hub:
            is_hub = True
        if city == dest:
            if is_hub:
                answer += 1
            continue
        arr = obj[city]
        for i in arr:
            q.append((i, is_hub))

    return answer % 10007


print(solution("SEOUL", "DAEGU", "YEOSU", [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]))
print(solution("ULSAN", "SEOUL", "BUSAN", [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]))