def solution(polynomial):
    express = polynomial.replace(" ", "").split("+")
    coff = 0
    num = 0

    for i in express:
        if "x" in i:
            coff = coff + int(i[:-1]) if i != "x" else coff + 1
        else:
            num += int(i)

    if coff>0:
        result = str(coff) + "x" if coff>1 else "x"
        result = result + " + " + str(num) if num>0 else result
    else:
        result = str(num)
    return result
