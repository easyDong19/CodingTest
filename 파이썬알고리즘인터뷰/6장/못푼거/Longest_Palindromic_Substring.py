#6장 6번
#해설을 봄
#투포인터를 활용해야하며 LCS문제임(최장공통부분문자열)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right]

        #해당사항이 없을 때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i,i+1), expand(i,i+2), key=len)

        return result