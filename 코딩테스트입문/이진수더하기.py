def solution(babbling):
    canAccent = ["aya","ye","woo","ma"]
    count = 0
    for i in babbling:
        for x in canAccent:
            if x in i and 2*x not in i:
                i = i.replace(x, ' ')
        if len(i.strip()) == 0:
            count+=1
    return count

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))

