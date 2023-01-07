class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        left = []
        right = []
        p = 1
        for i in range(len(nums)):
            left.append(p)
            p = p * nums[i]

        p = 1
        for i in range(len(nums)-1,-1,-1):
            right.append(p)
            p = p *nums[i]

        right = right[::-1]

        result = []
        for i in range(len(nums)):
            result.append(left[i]*right[i])

        return result



