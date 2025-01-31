from collections import Counter

class Solution:
    # Jenisa
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Counter = Counter(nums1)
        nums2Counter = Counter(nums2)

        common = nums1Counter & nums2Counter
        listCommon = list(common.elements())
        
        return listCommon