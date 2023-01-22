def dp(n):
    d = [0] * (n+1)

    for i in range(2,n+1):
        #1개씩 빼는 경우
        d[i] = d[i-1]+1
        if i%3 == 0:
            d[i] = min(d[i],d[i//3] + 1)
        if i%2 == 0:
            d[i] = min(d[i],d[i//2]+1)

    return d[i]

print(dp(10))
