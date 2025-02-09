import math
class Solution:
    # Jenisa
    def countBadPairs(self, nums: List[int]) -> int:
        # j - i != nums[j] - nums[i] ==> 
        # ==> nums[i] - i != nums[j] - j
        count = []
        diff = dict()
    
        for i in range(len(nums)):
            if nums[i] - i not in diff:
                diff[nums[i] - i] = 1
            else:
                diff[nums[i] - i] += 1
                if nums[i] -i not in count:
                    count.append(nums[i] - i)

        totalPairs = math.comb(len(nums), 2)
        for j in count:
            totalPairs -= math.comb(diff[j],2)
        

        return totalPairs