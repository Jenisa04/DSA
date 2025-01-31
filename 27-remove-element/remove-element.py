class Solution:
    # Jenisa
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0 #counter to keep track of nuber of elements in nums which aren't val
        
        temp = []
        for i in range(len(nums)):
            if nums[i] != val:
                count += 1
                temp.append(nums[i])
            else:
                nums[i] = -1 # remove the occurence of val in nums
            
        for i in range(len(temp)):
            nums[i] = temp[i]

        return count