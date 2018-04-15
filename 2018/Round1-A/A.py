

waffle_dict={'.':0,'@':1}
def waffle(c):
    return waffle_dict[c]

def sum_waffle(v):
    return sum([sum(a) for a in v])
def solve():
    r,c,h,v=map(int,input().split())
    plate=r*[c*[0]]
    for i in range(r):
        plate[i]=list(map(waffle,list(input())))
    total_choclates=sum_waffle(plate)
    total_diners=(h+1)*(v+1)
    if total_choclates%(total_diners) !=0:
        return 'IMPOSSIBLE'
    each_diner=total_choclates//total_diners
    chocs_in_rows=each_diner*(v+1)
    h_cut=[]
    b=0
    for i in range(h):
        s=0
        for j in range(b,r):
            s+=sum(plate[j])
            if s == chocs_in_rows:
                break
        else:
            return 'IMPOSSIBLE'
        b=j+1
        h_cut.append(j)
    chocs_in_cols=each_diner*(h+1)
    v_cut=[]
    b=0
    for i in range(v):
        s=0
        for j in range(b,c):
            s+=sum([p[j] for p in plate])
            if s == chocs_in_cols:
                break
        else:
            return 'IMPOSSIBLE'
        b=j+1
        v_cut.append(j)
    b_h=0
    b_v=0
    for h_c in range(h):
        b_v=0
        for v_c in range(v):
            if sum_waffle([p[b_v:v_cut[v_c]+1] for p in plate[b_h:h_cut[h_c]+1]])!=each_diner:
                return 'IMPOSSIBLE'
            b_v=v_cut[v_c]+1
        b_h=h_cut[h_c]+1
    h_cut.append(r-1)
    b=0
    for i in range(h+1):
        if sum_waffle([p[v_cut[v_c]+1:] for p in plate[b:h_cut[i]+1]])!=each_diner:
                return 'IMPOSSIBLE'
        b=h_cut[i]+1
    return 'POSSIBLE'




    


if __name__=='__main__':
    T=int(input())
    for i in range(T):
        print("Case #{}: {}".format(i+1, solve()))