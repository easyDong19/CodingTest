def solution(my_string):
    calc = list(my_string.split(" "))
    answer = int(calc[0])
    oper = ""
    for i in calc[1:]:
        if i.isdigit():
            if oper=="+":
                answer += int(i)
            else:
                answer -= int(i)
        else:
            oper=i

    return answer
