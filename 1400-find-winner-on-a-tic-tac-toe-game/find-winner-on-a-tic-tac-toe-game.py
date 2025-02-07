class Solution(object):
    # Jenisa
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        if (len(moves) < 5):
            return 'Pending'

        n = 3
        #3 rows and 3 columns
        # 0,1,2 is 0,1,2 rows and 3,4,5 is 0,1,2 columns
        gridSum = [0] * 6  
        diag1, diag2 = 0, 0
        player = 1 
        #start with player 'A' always 1; player 'B' is -1

        # iterate through all moves
        for row, col in moves:
            gridSum[row] += player
            gridSum[col+3] += player
            if row==col:
                diag1 += player
            if row+col==n-1:
                diag2 += player
            
            if max(abs(gridSum[row]), abs(gridSum[col+3]), abs(diag1), abs(diag2)) == 3:
                return "A" if player==1 else "B"

            player *= -1

        if (len(moves) == n*n):
            return "Draw"
        else:
            return 'Pending'