def dfs(obj, city, hub, dest, cases, visit_hub):
    res = 0
    if city == dest:
        if city in visit_hub:
            return 1
        else:
            return 0
    arr = obj[city]
    for i in arr:
        if i in visit_hub:
            if city in visit_hub:
                if cases.get(i) is None:
                    res += (dfs(obj, i, hub, dest, cases, visit_hub) % 10007)
                else:
                    res += (cases.get(i) % 10007)
            else:
                if i == hub:
                    if cases.get(i) is None:
                        res += (dfs(obj, i, hub, dest, cases, visit_hub) % 10007)
                    else:
                        res += (cases.get(i) % 10007)
        else:
            res += (dfs(obj, i, hub, dest, cases, visit_hub) % 10007)

    cases[city] = res
    return res


def solution(depar, hub, dest, roads):
    visit_hub = []
    cases = {}
    obj = {}
    visit_hub.append(hub)

    for r in roads:
        if obj.get(r[0]):
            obj[r[0]].append(r[1])
        elif obj.get(r[0]) is None:
            obj[r[0]] = [r[1]]
        if r[0] in visit_hub and r[1] not in visit_hub:
            visit_hub.append(r[1])

    tmp = -1
    if depar in visit_hub:
        tmp = visit_hub.index(depar)
    if tmp > -1:
        del visit_hub[tmp]

    answer = dfs(obj, depar, hub, dest, cases, visit_hub)
    return answer


print(solution("SEOUL", "DAEGU", "YEOSU", [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]))
print(solution("ULSAN", "SEOUL", "BUSAN", [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]))