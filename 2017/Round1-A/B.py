from math import ceil, floor

def solve(n,p):
    recipe = list(map(int,input().split()))
    ing=n*[None]
    rng=n*[[]]

    for i in range(n):
        ing[i]=sorted(list(map(int,input().split())))
        tmp=[]
        for j in range(p):
            tmp.append((ceil(ing[i][j]/recipe[i]/1.1),floor(ing[i][j]/recipe[i]/0.9)))
        rng[i]=tmp
    cnt=0
    for i in range(p):
        t=rng[0][i]
        if t[0]>t[1]:
            continue
        for k in range(1,n):
            for p in rng[k]:
                if (t[0]>=p[0] and t[0]<=p[1]) or (t[1]>=p[0] and t[1]<=p[1]):
                    rng[k].remove(p)
                    break
            else:
                break
        else:
            cnt+=1
    return cnt






if __name__=='__main__':
    T=int(input())
    for i in range(T):
        n,p=map(int,input().split())
        print("Case #%d: %d"%(i+1,solve(n,p)))