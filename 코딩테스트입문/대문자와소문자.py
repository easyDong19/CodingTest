def solution(my_string):
    answer = ''
    for word in my_string:
        if word.isupper():
            answer += word.lower()
        else:
            answer += word.upper()
    return answer

print(solution("aaaBBBB"))