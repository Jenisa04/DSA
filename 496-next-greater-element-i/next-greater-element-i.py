class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        # traverse over nums1 first
        for i in range(len(nums1)):
            temp = -1
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:                    
                    for k in range(j, len(nums2)):
                        if nums2[k] > nums2[j]:
                            temp = nums2[k]
                            break
            res.append(temp)

        return res