claps = ["3","6","9"]
def solution(order):
    answer = 0

    for word in str(order):
        if word in claps:
            answer += 1

    return answer


print(solution(33333))