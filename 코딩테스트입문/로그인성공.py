def solution(id_pw, db):
    for check in db:
        if check[0] == id_pw[0]:
            if check[1] == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"

print(solution(["meosseugi", "1234"],[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))