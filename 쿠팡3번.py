def solution(k, score):
    arr = [0] * (len(score))
    for i in range(len(score)-1):
        arr[i+1] = score[i] - score[i+1]
    arr.sort()

    cnt = 1
    find = True
    while find:
        find = False
        while cnt < len(arr):
            if arr.count(arr[cnt]) >= k:
                find = True
                for i in range(cnt, cnt + arr.count(arr[cnt])):
                    arr.pop(cnt)
            else:
                cnt += 1

    return len(arr[1:])-1


print(solution(3, [24,22,20,10,5,3,2,1]))
print(solution(2, [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]))