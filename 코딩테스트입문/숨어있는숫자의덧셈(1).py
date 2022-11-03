def solution(my_string):
    arr = list(my_string)
    answer = 0
    for word in arr:
        if word.isdigit():
            answer += int(word)

    return answer

