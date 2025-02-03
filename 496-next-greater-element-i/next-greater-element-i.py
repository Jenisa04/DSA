class Solution:
    # Jenisa
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Approach:
        # create empty hashmap that stores the greater than value for each element in nums2 else -1
        # traverse over nums2
        res = []
        ctr = dict()
        for i in range(len(nums2)):
            ctr[nums2[i]] = -1
            for j in range(i, len(nums2)):
                if nums2[j] > nums2[i]:
                    ctr[nums2[i]] = nums2[j]
                    break
        # now traverse over nums1 and find the next largest element from hashmap
        for idx, val in enumerate(nums1):
            res.append(ctr[val])
        return res