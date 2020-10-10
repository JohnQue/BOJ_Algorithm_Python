def solution(k, score):
    arr = [0] * (len(score))
    obj = {}
    for i in range(len(score)-1):
        arr[i+1] = score[i] - score[i+1]
        if obj.get(arr[i+1]) is None:
            obj[arr[i+1]] = 1
        elif obj.get(arr[i+1]):
            obj[arr[i+1]] += 1
    for key in obj.keys():
        if obj[key] >= k:
            obj[key] = 0

    answer = 0
    for value in obj.values():
        if value:
            answer += value

    return answer - 1


print(solution(3, [24,22,20,10,5,3,2,1]))
print(solution(2, [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]))
