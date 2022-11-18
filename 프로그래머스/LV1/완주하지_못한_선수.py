def solution(participant, completion):
    completion_list = {}
    for x in completion:
        if x in completion_list:
            completion_list[x] += 1
        else:
            completion_list[x] = 1

    for y in participant:
        if not y in completion_list: return y
        completion_list[y] -= 1
        if completion_list[y] == -1: return y

import collections
def smart_solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

def smart_solution2(participant, completion):
    marathon = {}
    hash_sum = 0
    for p in participant:
        marathon[hash(p)] = p
        hash_sum += hash(p)
    for c in completion:
        hash_sum -= hash(c)
    answer = marathon[hash_sum]
    return answer