vowel = ['a','e','i','o','u']

def solution(my_string):
    answer = ''
    for word in my_string:
        if not word in vowel:
            answer+=word
    return answer