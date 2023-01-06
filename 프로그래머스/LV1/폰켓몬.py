def solution(nums):
    phonekemon = {}
    for i in nums:
        if i in phonekemon:
            phonekemon[i] += 1
        else:
            phonekemon[i] = 1

    if len(nums)//2 <= len(phonekemon):
        return (len(nums)//2)
    else:
        return (len(phonekemon))


def smart_solution(ls):
    return min(len(ls)/2, len(set(ls)))

