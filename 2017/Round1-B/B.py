
colors={'R':1,'O':2,'Y':3,'G':4,'B':5,'V':6}

def fill_stable(previous,r,o,y,g,b,v, first=-1):
    if r > 0 and (previous in [-1,3,4,5]) and (first in [-1,3,4,5]):
        r-=1
        s='R'
    elif o > 0 and (previous in [-1,5]) and (first in [-1,5]):
        o-=1
        s='O'
    elif y>0 and  (previous in [-1,1,5,6]) and (first in [-1,1,5,6]):
        y-=1
        s='Y'
    elif g>0 and previous in [-1,1] and first in [-1,1]:
        g-=1
        s='G'
    elif b>0 and (previous in [-1,1,2,3]) and (first in [-1,1,2,3]):
        b-=1
        s='B'
    elif v>0 and previous in [-1,3] and first in [-1,3]:
        v-=1
        s='V'
    else:
        s='N'
    return s,r,o,y,g,b,v

def solve():
    n,r,o,y,g,b,v=map(int,input().split())
    stable=n*[-1]
    # first things first
    index=0
    for i in range(o):
        if b <2:
            return "IMPOSSIBLE"
        stable[3*i]='O'
        stable[3*i+1]='B'
        stable[3*i-1]='B'
        b-=2
    index=3*o
    if index > n-2:
        return "IMPOSSIBLE"
    for i in range(g):
        if r<2:
            return "IMPOSSIBLE"
        stable[index+3*i]='G'
        stable[index+3*i+1]='R'
        stable[index+3*i-1]='R'
        r-=2
    index+=3*g
    for i in range(v):
        if y<2:
            return "IMPOSSIBLE"
        stable[index+3*i]='V'
        stable[index+3*i+1]='Y'
        stable[index+3*i-1]='Y'
        y-=2
    index+=3*v
    if index:
        index-=1
    m=max([r,y,b])
    if m==r:
        for i in range(r):
            i=index+3*i
            if i>n-2:
                return "IMPOSSIBLE"
            stable[i]='R'
        r-=m
    elif m==y:
        for i in range(y):
            i=index+3*i
            if i>n-2:
                return "IMPOSSIBLE"
            stable[i]='Y'
        y-=m
    elif m==b:
        for i in range(b):
            i=index+3*i
            if i>n-2:
                return "IMPOSSIBLE"
            stable[i]='B'
        b-=m
    for i in range(r):
        i=index+3*i
        if i>n-1:
            return "IMPOSSIBLE"
        stable[i]='R'


    first=-1
    previous=-1
    for i in range(n-1):
        stable[i],r,o,y,g,b,v=fill_stable(previous,r,o,y,g,b,v)
        try:
            previous=colors[stable[i]]
        except KeyError:
            return "IMPOSSIBLE"
        if i == 0:
            first=previous
    stable[n-1],r,o,y,g,b,v=fill_stable(previous,r,o,y,g,b,v,first)
    if stable[n-1]=='N':
        return "IMPOSSIBLE"
    return ''.join(stable)
    
    



if __name__=='__main__':
    T=int(input())
    for i in range(T):
        print("Case #{}: {}".format(i+1, solve()))