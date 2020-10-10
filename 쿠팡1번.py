n = int(input())
max_value = 0
max_idx = 0
for i in range(2, 11):
    tmp = n
    ans = 1
    while tmp > 1:
        if tmp % i:
            ans *= (tmp % i)
        tmp //= i
    if max_value <= ans:
        max_value = ans
        max_idx = i
res = [max_idx, max_value]
print(res)
