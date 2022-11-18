#7장 1번
#두수의 합

#내풀이
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index,tar in enumerate(nums,0):
            if target-tar in nums[index+1:]:
                nums[index] = "PASS"
                return [index, nums.index(target-tar)]

    # 책 풀이 1. 브루트 포스
    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    # 책 풀이 2. in을 활용
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i+1:]:
                return [nums.index(n),nums[i+1:].index(complement)+(i+1)]

    #책 풀이 3. 첫 번째 수를 뺀 결과 키 조회
    def twoSum3(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]:
                return [i, nums_map[target - num]]

    #책풀이 4. 구조 개선
    def twoSum4(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        #하나로 통합
        for i, num in enumerate(nums):
            if target-num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i

    #책풀이 5. 투포인터
    #문제는 nums는 정렬된 값이 아니기 때문에 투포인트를 쓰면 안됨 그렇다고 쓰기위해 정렬하면 인덱스가 섞여버려 엉망이 된다.
    def twoSum5(self, nums: list[int], target: int) -> list[int]:
        left, right = 0, len(nums) - 1
        while not left == right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]


#최악의 방법인 브루트 포스는 피했지만 그럼에도 약간 부족한 듯한 코드. 3번이 가장 깔끔해보임.


