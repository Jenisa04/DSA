from collections import Counter

class Solution:
    # Jenisa
    def majorityElement(self, nums: List[int]) -> int:
        numsCounter = Counter(nums)
        element, count = numsCounter.most_common(1)[0]
        if count > (len(nums) // 2):
            return element