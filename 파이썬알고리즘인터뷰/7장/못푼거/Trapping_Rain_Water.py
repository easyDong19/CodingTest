# 7장 8번
class Solution:
    # 책에서 풀이 1. 투포인트 활용 종으로 처리 좀더 직관
    def trap1(self, height: list[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume

    # 책에서 풀이 2. 스택 샇기 횡으로 처리
    # 직관적으로 매우 이해하기 힘들다
    def trap2(self, height: list[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                #양옆으로 막혀있지 않다
                if not len(stack): break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
        return volume

test = Solution()
arr = [0,1,0,2,1,0,1,3,2,1,2,1]
test.trap2(arr)
