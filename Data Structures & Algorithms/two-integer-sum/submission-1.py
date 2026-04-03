class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        l = len(nums)
        for i in range(l):
            diff = target - nums[i]
            if diff in dict: 
                return [dict[diff], i]
            else:
                dict[nums[i]] = i