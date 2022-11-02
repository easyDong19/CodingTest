def solution(box, n):
    row = box[0]//n
    col = box[1]//n
    height  = box[2]//n
    return row*col*height

print(solution([1,1,1],1))
print(solution([10,8,6],3))

