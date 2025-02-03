class Solution:
    # Jenisa
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array first
        nums.sort()
        result = []
        for m, n in enumerate(nums):
            if m > 0 and n == nums[m-1]:
                continue
            l, r = m+1, len(nums) - 1
            while l < r:
                total = n + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    result.append([n,nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result