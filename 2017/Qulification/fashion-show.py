import numpy as np
import os
from tqdm import tqdm
from copy import deepcopy

model_dict={'+':1,'x':2,'o':3, '.':0}

def get_instance_info_line(line):
    n,m=line.split()
    n,m=int(n),int(m)
    matrix=np.zeros((n,n))
    return matrix,m

def place_model_number(line,matrx):
    line_split = line.split()
    model_number=model_dict[line_split[0]]
    r,c=(int(line_split[1])-1),(int(line_split[2])-1)
    matrx[r,c]=model_number


def read_input(path):
    with open(path) as fhandler:
        number_of_instances=int(fhandler.readline().strip())
        cells=[None]*number_of_instances
        for i,line in enumerate(fhandler):
            cells[i],m=get_instance_info_line(line)
            for j in range(m):
                place_model_number(fhandler.readline().strip(),cells[i])
    return cells

def get_input():
    number_of_instances=int(input())
    for _ in range(1,number_of_instances+1):
        matrix,m=get_instance_info_line(input())
        for i in range(m):
            place_model_number(input(),matrix)
        yield matrix

def find_all_diags(n):
    diags=[None]*n**2
    i=0
    for r in range(n):
        for c in range(n):
            position=(r,c)
            _,t = get_diagonal_indexes(n,position)
            diags[i]=[(position,t)]
            i+=1
    diags = sorted(diags,key=lambda p:p[0][1])
    return diags

def get_points(cell):
    return (cell>0).sum()+(cell==3).sum()

def upgrade_model(matrix):
    n=len(matrix)
    indx=np.arange(n)
    indx=np.floor((indx+1)/2)*np.power(-1,indx)
    indx=indx.astype(int)
    x,y=np.where(matrix!=-1)
    diags=find_all_diags(n)
    for position in diags:
        position=position[0][0]
        # r=i
        # if r <0:
        #     r+=n
        # for c in range(n):
            # position=(r,c)
        old_mode=matrix[position]
        matrix[position]=1
        if not check_rules(matrix,position):
            matrix[position]=old_mode
        else:
            if old_mode>1:
                matrix[position]=3
    # x,y=np.where(matrix==0)
    for i in indx:
        # r,c=x[i],y[i]
        r=i
        if r<0:
            r+=n
        for c in range(n):
            position=(r,c)
            old_mode=matrix[position]
            matrix[position]=2
            if not check_rules(matrix,position):
                matrix[position]=old_mode
            else:
                if old_mode!=0 and old_mode!=2:
                    matrix[position]=3
        
    return matrix

def get_diagonal_indexes(n,position):
    r,c=position
    n-=1
    counts = (n+1)#+2*(min(n-c,c))
    indexes=[(-np.ones(counts),-np.ones(counts))]*2
    j=0
    for i in range(n+1):
        if r+c-i <= n and r+c>=i:
            indexes[0][0][j],indexes[0][1][j]=i,r+c-i
            j+=1
    indexes[0]=(indexes[0][0][:j].astype(int),indexes[0][1][:j].astype(int))
    t=j
    j=0
    for i in range(n+1):
        if c-r<=n-i and c-r+i >= 0:
            indexes[1][0][j],indexes[1][1][j]=i,c-r+i
            j+=1
    indexes[1]=(indexes[1][0][:j].astype(int),indexes[1][1][:j].astype(int))
    t+=j-1
    return indexes,t
    

def check_rules(matrix, position):
    n=matrix.shape[0]
    diagonals,_=get_diagonal_indexes(n,position)
    r,c=position
    rule_1=(matrix[r,:]==2).sum()+(matrix[r,:]==3).sum() + (matrix[:,c]==2).sum()+(matrix[:,c]==3).sum()-1
    rule_2=max((matrix[diagonals[0]]==1).sum() + (matrix[diagonals[0]]==3).sum(),(matrix[diagonals[1]]==1).sum() + (matrix[diagonals[1]]==3).sum())
    if rule_1 > 1 or rule_2>1:
        return False
    else:
        return True

def get_changes(old_matrix,new_matrix):
    x,y=np.where((old_matrix-new_matrix)!=0)
    return x,y


def change_placed_models(matrix):
    x,y=np.nonzero(matrix)
    for i in range(len(x)):
        position=(x[i],y[i])
        past_value=matrix[position]
        matrix[position]=3
        if not check_rules(matrix,position):
            matrix[position]=past_value
    return matrix



from collections import defaultdict
def run_test(test_iteration):
    N, M = map(int, input().split())
    start_grid = [['.' for x in range(N)] for y in range(N)]
    free_rows = set(range(N))
    free_cols = set(range(N))
    # use sum = r + c, diff = r - c coords for diagonals
    free_sum = set(range(2 * N - 1))
    free_diff = set(range(- N + 1, N))
    for i in range(M):
        m, r, c = input().split()
        r, c = int(r) - 1, int(c) - 1
        start_grid[r][c] = m
        if m in {'x', 'o'}:
            assert r in free_rows and c in free_cols
            free_rows.remove(r)
            free_cols.remove(c)
        if m in {'+', 'o'}:
            assert r + c in free_sum and r - c in free_diff
            free_sum.remove(r + c)
            free_diff.remove(r - c)
    new_grid = [row[:] for row in start_grid]
    assert len(free_rows) == len(free_cols)
    for r, c in zip(free_rows, free_cols):
        # add vertical component x
        if new_grid[r][c] == '+':
            new_grid[r][c] = 'o'
        elif new_grid[r][c] == '.':
            new_grid[r][c] = 'x'
        else:
            assert False
    squares_by_sum, squares_by_diff = defaultdict(list), defaultdict(list)
    for r in range(N):
        for c in range(N):
            squares_by_sum[r + c].append((r,c))
            squares_by_diff[r - c].append((r,c))
    for i in range(2 * N - 1):
        squares_by_sum[i].sort(key=lambda p:len(squares_by_diff[p[0] - p[1]]))
    for i in range(- N + 1, N):
        squares_by_diff[i].sort(key=lambda p:len(squares_by_sum[p[0] + p[1]]))
    for s in sorted(range(2 * N - 1), key=lambda s:len(squares_by_sum[s])):
        if s not in free_sum: continue
        assert s in free_sum
        for p in reversed(squares_by_sum[s]):
            r, c = p
            assert r + c == s
            assert s in free_sum
            assert r + c in free_sum
            if r - c not in free_diff: continue
            # add diagonal component +
            if new_grid[r][c] == 'x':
                new_grid[r][c] = 'o'
            elif new_grid[r][c] == '.':
                new_grid[r][c] = '+'
            else:
                assert False
            # mark used
            free_sum.remove(r + c)
            free_diff.remove(r - c)
            break
    # Finish up
    score = 0
    changelist = []
    for r in range(N):
        for c in range(N):
            if new_grid[r][c] in {'x', 'o'}:
                score += 1
            if new_grid[r][c] in {'+', 'o'}:
                score += 1
            if new_grid[r][c] != start_grid[r][c]:
                changelist.append((r,c))
    print("Case #{}: {} {}".format(test_iteration, score, len(changelist)))
    for r,c in changelist:
        print(new_grid[r][c], r + 1, c + 1)

    new_grid=np.array([[model_dict[c] for c in row] for row in new_grid])
    print(new_grid.T)


if __name__ == '__main__':
    # i=input()
    # run_test(0)
    # exit()
    path=os.path.join(os.path.dirname(__file__), 'D-large-practice.in')
    # path='input'
    cells=read_input(path)
    with open(os.path.join(os.path.dirname(__file__), 'D-large-practice.out'), 'w') as fh:
        for i,matrix in tqdm(enumerate(read_input(path))):
            old_matrix=deepcopy(matrix)
            # matrix=change_placed_models(matrix)
            matrix=upgrade_model(matrix)
            # matrix=change_placed_models(matrix)
            matrix=matrix.astype(int)
            score=get_points(matrix)
            x,y=get_changes(old_matrix,matrix)
            num_changes=len(x)
            b=list(model_dict.keys())
            string='Case #%d: %d %d\n'%(i+1,score,num_changes)
            for j in range(num_changes):
                m=b[matrix[x[j],y[j]]-1]
                string += '%s %d %d\n'%(m,x[j]+1,y[j]+1)
            fh.write(string)
            
        
            
    # print("first 3 instances are ", cells[:3])
    # n=3
    # position=(1,2)
    # diagonals=get_diagonal_indexes(n=n,position=position)
    # print("n", n, "position", position, "diagonals", diagonals)
    # matrix=np.array([[0,0,0],[1,1,1],[2,0,0]])
    matrix=np.zeros((5,5))
    matrix=np.array([[1,0,1,0,1],
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]])
#     [[3 1 1 1 1 1 1 1]
#  [0 2 0 0 0 0 0 0]
#  [0 0 2 0 0 0 0 0]
#  [0 0 0 2 0 0 0 0]
#  [0 0 0 0 2 0 0 0]
#  [0 0 0 0 0 2 0 0]
#  [0 0 0 0 0 0 2 0]
#  [0 1 1 1 1 1 1 2]]
    # matrix=cells[0]
    # matrix=np.array([[1,0,1,1,1,1,1,1],
    #                  [0,0,2,0,0,0,0,0],
    #                  [0,0,0,2,0,0,0,0],
    #                  [0,0,0,0,2,0,0,0],
    #                  [0,0,0,0,0,2,0,0],
    #                  [2,0,0,0,0,0,0,0],
    #                  [0,0,0,0,0,0,2,0],
    #                  [0,1,1,1,1,1,1,0]])
    old_matrix=deepcopy(matrix)
    # print("matrix", matrix, matrix.shape)
    # change_placed_models(matrix)
    # print("change placed model matrix", change_placed_models(matrix))
    # matrix=np.array([[0,0],[0,0]])
    print("matrix", matrix.shape)
    # upgrade_model(matrix)
    matrix=change_placed_models(matrix)
    matrix=upgrade_model(matrix)

    # print("upgrade matrix", upgrade_model(matrix))
    # print("change placed model matrix", change_placed_models(matrix))
    # change_placed_models(matrix)
    score=get_points(matrix)
    matrix=matrix.astype(int)
    print("score is %d"%(score))
    x,y=get_changes(old_matrix,matrix)
    num_changes=len(x)
    b=list(model_dict.keys())
    string='Case #%d: %d %d\n'%(1,score,num_changes)
    for j in range(num_changes):
        m=b[matrix[x[j],y[j]]-1]
        string += '%s %d %d\n'%(m,x[j]+1,y[j]+1)
    print(string)
    print(matrix)
