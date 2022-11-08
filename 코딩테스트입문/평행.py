def solution(dots):
    for i,j,x,y in [(0,1,2,3),(0,2,1,3),(0,3,1,2)]:
        dx = dots[i][0] - dots[j][0]
        dy = dots[i][1] - dots[j][1]
        slop1 = dy / dx

        dx = dots[x][0] - dots[y][0]
        dy = dots[x][1] - dots[y][1]
        slop2 = dy / dx

        if slop1 == slop2: return 1
    return 0

def smart_solution(dots):
    ang = []
    for i in range(3):
        for j in range (i+1, 4):
            x= dots[i][0] - dots[j][0]
            y= dots[i][1] - dots[j][1]

            a = y/x if x!=0 else -1
            if a not in ang:
                ang.append(a)
            else:
                return 1
    return 0