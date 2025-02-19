class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat) * len(mat[0]):
            return mat
        nums = []
        for i in range(len(mat)):
            for j in mat[i]:
                nums.append(j)
        
        reshapeMat = []
        for row in range(r):
            reshapeMat.append(nums[(row*c) : (row+1)*c])
        
        return reshapeMat