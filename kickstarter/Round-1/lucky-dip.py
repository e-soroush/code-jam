from math import pow

def compute_expected(n,k,values):
    values=sorted(values)
    mean=sum(values)/n
    for _ in range(k):
        m=0
        for i,v in enumerate(reversed(values)):
            if v<=mean:
                break
            m+=v
        mean=((n-i)*mean+m)/n
    return mean



def test_res():
    n=5
    k=3
    values=[16,7,11,4,1]
    print('%.6f'%compute_expected(n,k,values))


if __name__=='__main__':
    # test_res()
    T=int(input())
    for i in range(T):
        n,k=map(int,(input()).split())
        values=list(map(int,input().split()))
        print('Case #%d: %.6f'%(i+1,compute_expected(n,k,values)))