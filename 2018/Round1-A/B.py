
def get_capacity(i,c,m,p,s):
    # capacity=c*[0]
    # for j in range(c):
        # capacity[j]=min(m[j],max(0,(i-p[j])//s[j]))
    capacity=sorted([min(m[j],max(0,(i-p[j])//s[j])) for j in range(c)],reverse=True)
    # capacity=sorted(capacity)
    return capacity

def sum_capacity(capacity, r):
    return sum(capacity[:r])

def solve():
    r,b,c=map(int,input().split())
    m=c*[None]
    s=c*[None]
    p=c*[None]
    for i in range(c):
        m[i],s[i],p[i]=map(int,input().split())
    
    T=2e18
    i=T//2
    l=0
    h=T
    while True:
        if h <l:
            i=l
            break
        capacity=get_capacity(i,c,m,p,s)
        if sum_capacity(capacity,r)>=b:
            # capacity=get_capacity(i-1,c,m,p,s)
            # if sum_capacity(capacity,r)<b:
            #     break
            # else:
            h=i-1
            i=(h+l)//2
                # continue
        else:
            # if sum_capacity(capacity,r)<b:
            #     capacity=get_capacity(i+1,c,m,p,s)
            #     if sum_capacity(capacity,r)>=b:
            #         i+=1
            #         break
            l=i+1
            i=(h+l)//2
            # continue

            

    return int(i)
    


if __name__=='__main__':
    T=int(input())
    for i in range(T):
        print("Case #{}: {}".format(i+1, solve()))