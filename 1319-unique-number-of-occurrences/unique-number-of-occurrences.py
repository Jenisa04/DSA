class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ctrMap = dict()
        l = 0
        r = len(arr) - 1

        while l <= r:
            if l == r:
                ctrMap[arr[l]] = ctrMap.get(arr[l], 0) + 1
            else:
                ctrMap[arr[l]] = ctrMap.get(arr[l], 0) + 1
                ctrMap[arr[r]] = ctrMap.get(arr[r], 0) + 1
            
            
            l+=1
            r-=1
        if len(ctrMap.values()) == len(set(ctrMap.values())):
            return True

        return False