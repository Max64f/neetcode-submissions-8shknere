class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        s = set()
        i = 0
        l = len(nums)
        while not flag and i != l: 
            if nums[i] not in s:
                s.add(nums[i])
                i += 1
            else:
                flag = True
        return flag 