
def solve():
    n=int(input())
    v=list(map(int,input().split()))
    while True:
        done=True
        for i in range(n-2):
            if v[i]>v[i+2]:
                v[i],v[i+2]=v[i+2],v[i]
                done=False
        if done:
            break
    sorted_v=sorted(v)
    if v==sorted_v:
        return 'OK'
    else:
        for i in range(n):
            if v[i]!=sorted_v[i]:
                break
        return i



if __name__=='__main__':
    T=int(input())
    for i in range(T):
        print("Case #{}: {}".format(i+1, solve()))