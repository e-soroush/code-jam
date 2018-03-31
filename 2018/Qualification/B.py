import sys

states=list(map(chr,range(65,91)))
def sum_p(p):
    return sum([p_i[1] for p_i in p])
def solve(n):
    p=[[states[i],p_i] for i,p_i in  enumerate(map(int,(input()).split()))]
    result=''
    while True:
        p=sorted(p,key=lambda f:f[1])
        if sum_p(p[:-1])>0.5!=0 and p[-1][1]/sum_p(p)>0.5:
            print('p ', p, file=sys.stderr)
        if p[-1][1]==0:
            break
        if p[-1][1]==p[-2][1]:
            if p[-1][1]==1:
                if sum_p(p[:-2]) != 1:
                    p[-1][1]=0
                    p[-2][1]=0    
                    result+=' %s%s'%(p[-1][0],p[-2][0])    
                    continue
                p[-1][1]=0
                result+=' %s'%p[-1][0]
            else:
                p[-1][1]-=1
                p[-2][1]-=1
                result+=' %s%s'%(p[-1][0],p[-2][0])
        else:
            if p[-1][1]==1:
                p[-1][1]=0
                result+=' %s'%p[-1][0]
                break
            else:
                p[-1][1]-=2
                result+=' %s%s'%(p[-1][0],p[-1][0])
    return result
                






if __name__=='__main__':
    T=int(input())
    for i in range(T):
        n=int(input())
        print("Case #%d: %s"%(i+1,solve(n)))