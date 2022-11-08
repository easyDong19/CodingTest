def solution(lines):
    answer = 0
    num_line = [0 for i in range(200)]
    for [a, b] in lines:
        for i in range(a, b):
            num_line[i + 100] += 1
    answer = num_line.count(2) + num_line.count(3)
    return answer


def smart_solution(lines):
    sets = [set(range(l,m)) for l,m in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])




