def solution(spell, dic):
    for word in dic:
        check = 0
        for i in spell:
            if i in word:
                check += 1
            if check == len(spell):
                return 1
    return 2


def smart_solution(spell, dic):
    spell = set(spell)
    for s in dic:
        #차집합 공집합이면 return 1을 반환
        if not spell-set(s):
            return 1
    return 2