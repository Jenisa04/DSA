from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        original_color = image[sr][sc]
        
        # Early exit if the starting color is the same as the target color
        if original_color == color:
            return image

        # Use a deque for optimized pop operations
        queue = deque([(sr, sc)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            if image[r][c] == original_color:
                image[r][c] = color
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == original_color:
                        queue.append((nr, nc))
                        
        return image
