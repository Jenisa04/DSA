import math
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # j - i != nums[j] - nums[i] ==> 
        # ==> nums[i] - i != nums[j] - j
        # count = []
        # diff = dict()
    
        # for i in range(len(nums)):
        #     if nums[i] - i not in diff:
        #         diff[nums[i] - i] = 1
        #     else:
        #         diff[nums[i] - i] += 1
        #         if nums[i] -i not in count:
        #             count.append(nums[i] - i)

        # totalPairs = (len(nums) * (len(nums) - 1)) // 2
        # for j in count:
        #     totalPairs -= math.comb(diff[j],2)
        
        # return totalPairs
        freq = {}
        good_pairs = 0

        for i, num in enumerate(nums):
            key = num - i
            good_pairs += freq.get(key, 0)
            freq[key] = freq.get(key, 0) + 1

        n = len(nums)
        return (n * (n - 1)) // 2 - good_pairs