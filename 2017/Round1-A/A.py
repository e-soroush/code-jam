from copy import deepcopy

def solve(r,c):
    board=r*[c*[None]]
    students=set()
    question_marks=[]
    for i in range(r):
        board[i]=list(input())
        for j,s in enumerate(board[i]):
            if s != '?':
                students.add(s)
            else:
                question_marks.append((i,j))
    tmp = deepcopy(board)
    
    for i in range(r):
        for j in range(c):
            if board[i][j]!='?':
                for jj in range(j+1,c):
                    if board[i][jj]=='?':
                        board[i][jj]=board[i][j]
                    else:
                        break
                for jj in range(j-1,-1,-1):
                    if board[i][jj]=='?':
                        board[i][jj]=board[i][j]
                    else:
                        break
    
    for i,row in enumerate(board[1:-1]):
        i+=1
        if not all([s!='?' for s in row]):
            for j in range(i-1,r):
                if all([s!='?' for s in board[j]]):
                    board[i]=board[j]
                    break
    if not all([s!='?' for s in board[-1]]):
        board[-1]=board[-2]
    if not all([s!='?' for s in board[0]]):
        board[0]=board[1]
        
    for row in board:
        print(''.join(row))
    if any([s=='?' for row in board for s in row]):
        print(tmp)
        print("voila")
    for row in board:
        for s in row:
            students.add(s)
    for i in range(r):
        for j in range(c):
            if board[i][j] in students:
                students.remove(board[i][j])
                jj=j
                ii=i
                for jj in range(j+1,c):
                    if board[i][jj]!=board[i][j]:
                        jj-=1
                        break
                for ii in range(i+1,r):
                    if board[ii][j]!=board[i][j]:
                        ii-=1
                        break
                cnt=len([s for row in board for s in row if s==board[i][j]])
                if (ii-i+1)*(jj-j+1)!=cnt:
                    print(tmp)
                    print("voila freq")
                
                                        

if __name__=='__main__':
    T=int(input())
    for i in range(T):
        r,c=map(int,input().split())
        print("Case #%d:"%(i+1))
        solve(r,c)