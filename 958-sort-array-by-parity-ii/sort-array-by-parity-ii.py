class Solution:
    # Jenisa
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        evenList= []
        oddList=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                evenList.append(nums[i])
            else:
                oddList.append(nums[i])

        res = []

        for k in range(len(evenList)):
            res.append(evenList[k])
            res.append(oddList[k])

        return res