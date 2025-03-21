from typing import List

class Solution:
    def findNeighbors(self, r, c, m, n) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        validNeighbors = []
        for dr, dc in directions:
            if self.isValid(r+dr, c+dc, m, n):
                validNeighbors.append([r+dr, c+dc])
        return validNeighbors
            
    def isValid(self, r, c, m, n) -> bool:
        return 0 <= r < m and 0 <= c < n

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        original_color = image[sr][sc]
        
        if original_color == color:
            return image

        queue = [[sr, sc]]
        visited = set()
        
        while queue:
            r, c = queue.pop(0)
            if (r, c) not in visited:
                image[r][c] = color
                visited.add((r, c))
                
                for nr, nc in self.findNeighbors(r, c, m, n):
                    if (nr, nc) not in visited and image[nr][nc] == original_color:
                        queue.append([nr, nc])
                        
        return image
