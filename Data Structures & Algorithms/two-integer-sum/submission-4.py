class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, val in enumerate(nums):
            difference = target - val
            if difference in nums[index + 1:]:
                return [index, index + 1 + nums[index+1:].index(difference)]

        return []