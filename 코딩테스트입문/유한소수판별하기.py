def gcd(a,b):
    if b==0: return a
    else: return gcd(b,a%b)

def factorization(n):
    i = 2
    arr = [1]
    while n!=1:
        if n%i == 0:
            arr.append(i)
            n = n//i
            continue
        i+=1
    return arr


def solution(a, b):
    divisor = gcd(a,b)
    b = b//divisor
    arr = factorization(b)
    print(arr)
    #2만 존재 or 5만 존재 or 2와5만 존재 or 1
    if 2 in arr or 5 in arr or b == 1:
        if not 3 in arr and not 7 in arr:
            return 1
    return 2

from math import gcd
def smart_solution(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2