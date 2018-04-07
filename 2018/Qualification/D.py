from math import cos, acos,pi,sin,sqrt
import sys

def find_angle(a):
    for i in range(46):
        p1=cos(pi/180*i)+cos(pi/180*(90-i))
        if p1>=a-1e-6 and p1 <=a+1e-6:
            r=pi/180*(i)
            break
        if p1>a-1e-6:
            step=0.5
            tmp=step
            i-=1
            r=pi/180*(i)
            p1=cos(pi/180*(i+tmp))+cos(pi/180*(90-i-tmp))
            diff=abs(a-p1)
            while diff > 1e-6:
                if p1>a:
                    tmp-=step
                    step/=2
                tmp+=step
                p1=cos(pi/180*(i+tmp))+cos(pi/180*(90-i-tmp))
                diff=abs(a-p1)
                r=pi/180*(i+tmp)
            break
    return r

def solve():
    a=float(input())
    if a<=sqrt(2)+1e-6:
        r=find_angle(a)
        c=cos(r)/2
        s=sin(r)/2
        
        # if s<1e-6:
        #     s=int(s)
        print("{} {} 0".format(c,s))
        print("{} {} 0".format(-s,c))
        print("0 0 0.5")
    else:
        b=a/sqrt(2)
        r=find_angle(b)
        c=cos(r)
        s=sin(r)
        print("{} {} {}".format(sqrt(2)/4,sqrt(2)/4,0))
        print("{} {} {}".format(-sqrt(2)/4*c,-sqrt(2)/4*c,s/2))
        print("{} {} {}".format(sqrt(2)/4*s,-sqrt(2)/4*s,c/2))
        

if __name__=='__main__':
    T=int(input())
    for i in range(T):
        print("Case #{}:".format(i+1))
        solve()