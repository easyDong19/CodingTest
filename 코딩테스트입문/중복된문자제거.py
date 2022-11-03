def solution(my_string):
    arr = list(my_string)
    cha = set(arr)
    answer = ''

    print(arr)
    for i in arr:
        if i in cha:
            answer+=i
            cha.remove(i)
    return answer
