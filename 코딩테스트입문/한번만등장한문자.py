from collections import Counter
from functools import reduce

def solution(s):

    answer = reduce(lambda acc, cur: acc + cur[0] ,filter(lambda x: x[1]==1,Counter(s).items()),"")
    answer= sorted(list(answer))
    return ''.join(s for s in answer)

def smart_solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer