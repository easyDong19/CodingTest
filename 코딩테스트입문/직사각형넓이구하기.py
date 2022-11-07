def solution(dots):
    standard = dots[0]
    height = 0
    width = 0
    for i in dots[1:]:
        if i[0] == standard[0]:
          height = abs(i[1]-standard[1])
        elif i[1]==standard[1]:
            width = abs(i[0]-standard[0])
    answer = height * width

    return answer

