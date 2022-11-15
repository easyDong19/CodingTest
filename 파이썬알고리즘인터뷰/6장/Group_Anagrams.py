#6장 5번
import collections
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        answer = collections.defaultdict(list)
        for str in strs:
            answer[''.join(sorted(str))].append(str)
        return list(answer.values())

