
def solve():
    n=int(input())
    v=list(map(int,input().split()))
    v_odd=sorted(v[1:len(v):2])
    v_even=sorted(v[:len(v):2])
    v_sorted=len(v)*[None]
    for i in range(len(v)):
        if i%2==0:
            v_sorted[i]=v_even[i//2]
        else:
            v_sorted[i]=v_odd[i//2]
    vv_sorted=sorted(v)
    if v_sorted==vv_sorted:
        return 'OK'
    else:
        for i in range(n):
            if v_sorted[i]!=vv_sorted[i]:
                break
        return i



if __name__=='__main__':
    T=int(input())
    for i in range(T):
        print("Case #{}: {}".format(i+1, solve()))