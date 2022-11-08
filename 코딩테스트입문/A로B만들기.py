def solution(before, after):
    befores = list(before)
    afters = list(after)

    for i in befores:
        if i in afters:
            afters.remove(i)
    if not afters:
        return 1
    else:
        return 0


def smart_solution(before, after):
    before=sorted(before)
    after=sorted(after)
    if before==after:
        return 1
    else:
        return 0