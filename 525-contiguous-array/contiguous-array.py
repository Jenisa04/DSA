class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # edge cases
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if sum(nums) == 1: return 2
            else: return 0
        
        mp = {}
        sum_val = 0
        max_len = 0
        for i, num in enumerate(nums):
            sum_val += 1 if num == 1 else -1
            if sum_val == 0:
                max_len = i + 1
            elif sum_val in mp:
                max_len = max(max_len, i - mp[sum_val])
            else:
                mp[sum_val] = i
        return max_len