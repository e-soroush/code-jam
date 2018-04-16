
def sides(c):
    t={'+':0,'-':1}
    return(t[c])

def solve():
    pancake=list(map(sides,list(input())))
    cnt=0
    i=0
    while True:
        if sum(pancake)==0:
            break
        c=pancake[i] 
        if c==0 and i!=0:
            pancake[:i]=(i)*[0]
            cnt+=1
            if sum(pancake)!=0:
                cnt+=1
                pancake[:i+1]=(i+1)*[1]
                for j in range(i+1,len(pancake)):
                    if pancake[j] == 0:
                        pancake[j]=1
                    else:
                        break
                i=j-1
            else:
                i+=1 # finish
            continue
        elif c==0:
            for j in range(i,len(pancake)):
                if pancake[j]==0:
                    pancake[j]=1
                else: 
                    break
            cnt+=1
            i=j-1
        else:
            if len(pancake)==sum(pancake):
                pancake=[0]*len(pancake)
                cnt+=1
            i+=1
    return cnt



if __name__=='__main__':
    T=int(input())
    for i in range(T):
        print("Case #{}: {}".format(i+1, solve()))