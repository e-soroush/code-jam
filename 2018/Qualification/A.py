

def find_damage(P):
    d=1
    total=0
    for c in P:
        if c=='S':
            total+=d 
        elif c=='C':
            d*=2
    return total

def solve():
    D,P=input().split()
    D=int(D)
    P=list(P)
    i=len(P)-2
    cnt=0
    while True:
        if find_damage(P)<=D:
            break
        if i==-1:
            cnt='IMPOSSIBLE'
            break
        if ''.join(P[i:i+2])=='CS':
            P[i],P[i+1]=P[i+1],P[i]
            cnt+=1
            i=len(P)-2
        else:
            i-=1

    return cnt




if __name__=='__main__':
    T=int(input())
    for i in range(T):
        print("Case #{}: {}".format(i+1, solve()))