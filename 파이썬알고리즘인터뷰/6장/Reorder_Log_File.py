#6장 3번 로그파일 재정렬

#내가 푼 답
class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letters, digits = [],[]
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:],x.split()[0]))

        return letters+digits






