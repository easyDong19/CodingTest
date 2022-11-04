def solution(cipher, code):
    answer = ''
    for i,word in enumerate(cipher,1):
        if i % code ==0:
            answer += word

    return answer

print(solution("dfjardstddetckdaccccdegk",4))