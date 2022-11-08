def solution(A, B):
    count = 0
    if A==B: return count
    for i in range(len(A)):
        A = A[-1]+A[0:-1]
        count+=1
        if A == B: return count

    return -1

