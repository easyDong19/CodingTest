def solution(score):
    result = list(map(lambda x: (x[0]+x[1])/2,score))
    ranks = sorted(result,reverse=True)
    dicts = {}
    for i,rank in enumerate(ranks):
        if not str(rank) in dicts:
            dicts[str(rank)] = i+1
    answer= list(map(lambda x: dicts[str(x)],result))
    return answer


