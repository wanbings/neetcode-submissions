class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hash:
                return [nums.index(difference), i]
            hash.append(nums[i])
        return hash