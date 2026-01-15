class Solution(object):
    def updateBoard(self, board, click):
        if board[click[0]][click[1]]=="M":
            board[click[0]][click[1]]="X"
            return board
        dirs = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]   
        def bfs(row,col):
            m = len(board)
            n = len(board[0])
            queue = deque()
            queue.append((row,col))
            while queue:
                r,c = queue.popleft()
                valid_neighbors=[]
                count=0
                for d in dirs:
                    nr,nc=r+d[0],c+d[1]
                    if 0<=nr<m and 0<=nc<n:
                        if board[nr][nc]=="M": count+=1
                        elif board[nr][nc]=="E":
                            valid_neighbors.append([nr,nc])
                if count==0:
                    board[r][c]="B"
                    for ni in valid_neighbors:
                        if board[ni[0]][ni[1]]=="E":
                            board[ni[0]][ni[1]]="B"
                            queue.append((ni[0],ni[1]))
                else: board[r][c] = str(count)
        bfs(click[0],click[1])
        return board
