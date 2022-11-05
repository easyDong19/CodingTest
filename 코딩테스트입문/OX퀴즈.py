def solution(quiz):
    answer = []

    judge = False
    for i in quiz:
        calc = i.split(" ")
        x = int(calc[0])
        oper = calc[1]
        y = int(calc[2])
        result = int(calc[4])

        if calc[1] == "+":
            judge = (x + y == result)
        else:
            judge = (x - y == result)
        if judge:
            answer.append("O")
        else:
            answer.append("X")
    return answer


def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)
def smart_solution(equations):
        return ["O" if valid(equation) else "X" for equation in equations]