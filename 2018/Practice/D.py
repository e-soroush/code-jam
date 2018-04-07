
def get_last_state(instance):

    empty,people = instance[0], instance[1]
    occupied=[0,(1+empty)]
    for _ in range(people):
        empty_stalls_between=[(i,v) for i,v in enumerate([occupied[i+1]-occupied[i] for i in range(len(occupied)-1)])]
        most_distan_index=max(empty_stalls_between,key=lambda f:f[1])[0]
        lef_most_distance=(occupied[most_distan_index+1]-occupied[most_distan_index])//2+occupied[most_distan_index]
        occupied.append(lef_most_distance)
        occupied=sorted(occupied)
    most_distan_index=occupied.index(lef_most_distance)
    ls=occupied[most_distan_index]-occupied[most_distan_index-1]-1
    rs=occupied[most_distan_index+1]-occupied[most_distan_index]-1

    return max(ls,rs), min(ls,rs)
    

def solve(instance):

    empty,people = instance[0], instance[1]
    if people == empty:
        return(0,0)
    if people == 1:
        return get_last_state((empty,people))
    if people %2 != 0:
        people-=1
        empty-=1
    people = people//2
    empty=empty//2
    return solve((empty,people))

if __name__=='__main__':
    T=int(input())
    for i in range(T):
        n,k=map(int,(input()).split())
        print("Case #%d: %s"%(i+1,' '.join([str(int(r)) for r in solve((n,k))])))
