
def get_capacity(i,c,m,p,s):
    capacity=c*[0]
    for j in range(c):
        capacity[j]=min(m[j],max(0,(i-p[j])//s[j]))
    capacity=sorted(capacity)
    return capacity

def sum_capacity(capacity, r):
    return sum(capacity[-1:-r-1:-1])

def solve():
    r,b,c=map(int,input().split())
    m=c*[None]
    s=c*[None]
    p=c*[None]
    for i in range(c):
        m[i],s[i],p[i]=map(int,input().split())
    
    tmp=c*[0]
    for i in range(c):
        tmp[i]=b*m[i]+p[i]
    T=max(tmp)
    i=T//2
    l=0
    h=T
    while True:
        capacity=get_capacity(i,c,m,p,s)
        if sum_capacity(capacity,r)>=b:
            capacity=get_capacity(i-1,c,m,p,s)
            if sum_capacity(capacity,r)<b:
                break
            else:
                h=i-1
                i=l+(i-l)//2
                continue
        else:
            l=i+1
            i=l+(h-i)//2
            continue

            

    return i
    


if __name__=='__main__':
    T=int(input())
    for i in range(T):
        print("Case #{}: {}".format(i+1, solve()))