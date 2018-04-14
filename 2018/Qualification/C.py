import sys
from math import ceil
from copy import deepcopy
def solve():
    a=int(input())
    print(a,file=sys.stderr)
    num_steps=ceil(a/3)-3
    v=3*[3*[0]]
    i=j=2
    for step in range(num_steps+1):
        while True:
            print("%d %d"%(i,j))
            print("sent: %d %d"%(i,j),file=sys.stderr)
            ip,jp=map(int,input().split())
            print("recieved: %d %d"%(ip,jp),file=sys.stderr)
            if ip<=0 or jp<=0:
                print("terminated with %d"%ip,file=sys.stderr)
                exit()
            tmp=deepcopy(v[ip-1])
            tmp[jp-1-step]=1
            v[ip-1]=tmp
            if sum([sum(a) for a in v])==9:
                v=[[1,1,0],[1,1,0],[1,1,0]]
                print("break",file=sys.stderr)
                j+=1
                break
            print(v,file=sys.stderr)
    # if a==10:
    #     R,C=(3+2),(4+2)
    # elif a==20:
    #     R,C=(4+2),(5+2)
    # elif a==200:
    #     R,C=(14+2),(15+2)
    # v=R*[C*[0]]
    # i=j=2
    # cnt=0
    # while True:
    #     print("%d %d"%(i,j))
    #     print("sent: %d %d"%(i,j),file=sys.stderr)
    #     ip,jp=map(int,input().split())
    #     print("recieved: %d %d"%(ip,jp),file=sys.stderr)
    #     if ip <=0 and jp<=0:
    #         break
    #     tmp=deepcopy(v[ip-1])
    #     tmp[jp-1]=1
    #     v[ip-1]=tmp
    #     for ii in range(1,len(v)-1):
    #         for jj in range(1,len(v[0])-1):
    #             if v[ii][jj]==0:
    #                 break
    #         else:
    #             continue
    #         break
    #     if v[ii][jj]!=0:
    #         if sum(v[0])!=len(v[0]) or sum(v[R-1])!=len(v[0]):
    #             for c in range(C):
    #                 if v[0][c]==0:
    #                     if c==0:
    #                         c+=1
    #                     elif c==C-1:
    #                         c-=1
    #                     ii,jj=1,c
    #                     break
    #                 elif v[R-1][c]==0:
    #                     if c==0:
    #                         c+=1
    #                     elif c==C-1:
    #                         c-=1
    #                     ii,jj=R-2,c
    #                     break
    #         else:
    #             for r in range(R):
    #                 if v[r][0]==0:
    #                     if r==0:
    #                         r+=1
    #                     elif r==R-1:
    #                         r-=1
    #                     ii,jj=r,1
    #                 elif v[r][C-1]==0:
    #                     if r==0:
    #                         r+=1
    #                     elif r==R-1:
    #                         r-=1
    #                     ii,jj=r,C-2
    #                     break
            

    #     i,j=ii+1,jj+1
    #     if cnt==1000-1:
    #         print('v',v,file=sys.stderr)
    #         exit()
    #     cnt+=1
    # print('cnt', cnt, file=sys.stderr)


if __name__=='__main__':
    T=int(input())
    for i in range(T):
        solve()