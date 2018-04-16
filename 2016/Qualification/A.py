from math import log10,ceil
def get_digits(n):
    return set(map(int,list(str(n))))

def solve(n):
    numbers=get_digits(n)
    p=10*10**(ceil(log10(n+1e-6)))
    for i in range(1,10**6):
        m=i*n
        # if m > p:
        #     m="INSOMNIA"
        #     break
        for c in str(m):
            numbers.add(int(c))
        if len(numbers)==10:
            break
    else:
        m="INSOMNIA"
        
    return m

if __name__=='__main__':
    T=int(input())
    for i in range(T):
        n=int(input())
        print("Case #{}: {}".format(i+1,solve(n)))