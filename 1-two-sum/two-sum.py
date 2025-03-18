class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for idx, num in enumerate(nums):
            if target-num in nums[idx+1:]:
                res.append(idx)
                idx2 = idx
                for j in nums[idx+1:]:
                    idx2+=1
                    if j == target-num:
                        res.append(idx2)
                        break
                break
        return res