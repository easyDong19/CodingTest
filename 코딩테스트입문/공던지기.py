def solution(numbers, k):
    length = len(numbers)
    index = 2
    repeat = [0]
    while index!=0:
        repeat.append(index)
        index+=2
        if index>length-1:
            index = index%length
    print(numbers[repeat[k%len(repeat)-1]])
    answer = 0
    return answer

#남이 짠 스마트 솔루션
def Smart_solution(numbers, k):
    #k번째에서 던진 사람이기에 k-1 한칸씩 건너띄므로 2를 곱해줌 그럼 2*(k-1)번째 사람이 던지는 사람이 됨
    #그중 numbers의 숫자만큼 반복됨
    #ex k=6이면 10번째 사람이 던지는 사람이 됨
    return 2 * (k - 1) % len(numbers) + 1