#230122 실패
def dp(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    return dp(n-1) + dp(n-2) + dp(n-3)

print(dp(5))
