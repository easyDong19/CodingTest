def solution(sides):
    answer = 0
    #가장 긴변이 slides에 있을 때
    line = max(sides)

    answer = answer + line - (max(sides)- min(sides))
    #가장 긴변이 slides에 없을 때
    line_sum = sum(sides)
    answer = answer + line_sum - max(sides) - 1
    return answer
