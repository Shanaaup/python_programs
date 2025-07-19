k=int(input())
chessboard=[[0 for _ in range(k)] for _ in range(k)]
def isattacking(i,j):
    for l in range(k):
        if chessborad[i][l]==1 or chessboard[i][j]==1:
            return True
    for l in range(k):
        for m in range(k):
            if l+m==i+j and chessboard[l][m]==1:
                return True
            if l-m==i-j and chessboard[l][m]==1:
                return True
    
def nquees(n):
    if n==0:
        return True
    for i in range(k):
        for j in range(k):
            if not isattacking(i,j) and chessboard[i][j]==0:
                chessboard[i][j]=1
                if nqueens(n-1):
                    return True
                chessborad[i][j]=0
    return False