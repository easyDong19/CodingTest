def solution(s):
    arr = list(s.split(" "))
    numbers = []
    answer = 0
    for word in arr:
        if word == "Z" and numbers:
            answer -= numbers.pop()
        elif word != "Z":
            numbers.append(int(word))

    return sum(numbers)

