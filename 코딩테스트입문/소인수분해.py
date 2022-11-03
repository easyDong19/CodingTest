import math
def solution(n):
    answer = []
    i=2
    while i<= int(math.sqrt(n)+1):
       if n%i==0:
           answer.append(i)
           n=n//i
       else:
           i+=1
    if n>1:
        answer.append(n)

    result1 = set(answer)
    result2 = list(result1)
    result2.sort()

    return result2

#남이 만든 코드
def smart_solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            #이 로직을 넣을 수 있었다는 점을 생각했어야 함
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer