from math import sqrt
import sys


def solve():
    n,p=map(int,input().split())
    cookies_width=n*[None]
    cookies_height=n*[None]
    for i in range(n):
        cookies_width[i],cookies_height[i]=map(int,input().split())
    current_p=2*(sum(cookies_width)+sum(cookies_height))
    diff=current_p
    selected_cookies=[]
    while True:
        if p <= current_p + 1e-6:
            break
        diff=min(diff,p-current_p)
        d=sys.maxsize
        selected=0
        s=0
        for i in range(n):
            if i in selected_cookies:
                continue
            d_max=diff-2*min(cookies_width[i],cookies_height[i])
            d_min=diff-2*sqrt(cookies_width[i]**2+cookies_height[i]**2)
            if d_max<0 and d_min < 0:
                continue
            if d_max>=0 and d_min <=0:
                d=0
                current_p=p
                break
            if d_min < d:
                d=d_min
                selected=i
        last_p=current_p
        last_p+=2*sqrt(cookies_width[i]**2+cookies_height[i]**2)
        if last_p>p+1e-6:
            break
        else:
            current_p=last_p
        selected_cookies.append(selected)
    return current_p



    

if __name__=='__main__':
    T=int(input())
    for i in range(T):
        print("Case #{}: {}".format(i+1, solve()))