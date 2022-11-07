def solution(my_string):
    my_string += "a"
    answer = 0
    num =""
    for word in my_string:
        if word.isdigit():
            num += word
        else:
            if num != "":
                answer += int(num)
                num = ""


    return answer

import re
#정규표현식 사용
def smart_solution(my_string):
    return sum([int(i) for i in re.findall(r'[0-9]+', my_string)])

print(solution("123"))