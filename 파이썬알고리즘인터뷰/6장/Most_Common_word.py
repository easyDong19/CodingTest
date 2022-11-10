# 6장 4번 가장 흔한 단어
import collections
import re
import string
from collections import Counter


# 내가 푼 답
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        for char in string.punctuation:
            paragraph = paragraph.replace(char, " ")

        letter = [word for word in paragraph.lower().split() if not word in banned]
        return Counter(letter).most_common(1)[0][0]


# 책에서 푼 답
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
                 if word not in banned]

        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
