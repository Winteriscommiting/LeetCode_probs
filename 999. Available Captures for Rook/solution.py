class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(len(board)):
            if 'R' in board[i]:
                r,c=i,board[i].index('R')
        res=0
        for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
            x,y=r+i,c+j
            while 0<=x<8 and 0<=y<8:
                if board[x][y]=='B':
                    break
                if board[x][y] == 'p':
                    res += 1
                    break
                x,y=x+i,y+j
        return res