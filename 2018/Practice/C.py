
def solve(k,n):
    max_hour=0
    for _ in range(n):
        k_i,s_i=map(int,(input()).split())
        hour=(k-k_i)/s_i
        if hour>max_hour:
            max_hour=hour
    return k/max_hour
    



if __name__=='__main__':
    T=int(input())
    for i in range(T):
        k,n=map(int,(input()).split())
        print('Case #%i: %.6f'%(i+1,solve(k,n)))
