from math import ceil

def solve(Hd,Ad,Hk,Ak,B,D):
    # first find attacking and buffing steps
    steps=ceil(Hk/Ad)
    for i in range(Hk):
        new_steps=i+1+ceil(Hk/(Ad+(i+1)*B))
        if new_steps>steps:
            break
        steps=new_steps
    # deteremine how to act
    free_atk=ceil(Hd/Ak)
    # if we have enough health to attack at the begining and win
    if free_atk >= steps:
        total_steps=steps
        return int(total_steps)
    
    if free_atk >2: # if we have enough health to some attack at start
        nsteps=steps-(2*(free_atk-1)) # attacking step is different at first and last steps
        if nsteps>0:
            total_steps = int(ceil(nsteps/(free_atk-2))+nsteps+(2*(free_atk-1)))+1
        else:
            total_steps = int(steps)+1
    else: # Else impossible unless we have debuffing it is impossible
        total_steps = "IMPOSSIBLE"
    if D == 0:
        return total_steps
    Hd_tmp=Hd
    j=0
    # start debuffing
    for i in range(Ak):
        tmp=Ak-(i+1)*D
        # compute health after debuffing
        Hd_tmp-=tmp
        if Hd_tmp-(Ak-(i+2)*D)<=0: # if next step is dying ensure to refill the health
            j+=1
            Hd_tmp=Hd-tmp # after refilling alwayse next step knight gonna reduce your health
        if tmp>0:
            free_atk=ceil((Hd)/tmp)
            if free_atk >2:
                nstep=steps-(ceil(Hd_tmp/tmp)-1)-(free_atk-1)
                if nstep>0:
                    new_steps=ceil(nstep/(free_atk-2))+nstep+1+i+j+(ceil(Hd_tmp/tmp)-1)+(free_atk-1)+1
                else:
                    if steps>(ceil(Hd_tmp/tmp)-1): j+=1
                    new_steps=steps+1+i+j
            elif free_atk==1:
                break
            else:
                new_steps = "IMPOSSIBLE"
        else:
            new_steps=steps+i+1+j
            if new_steps != "IMPOSSIBLE":
                if total_steps == "IMPOSSIBLE":
                    total_steps=int(new_steps)
                elif new_steps < total_steps:
                    total_steps=int(new_steps)
            break
        
        if new_steps != "IMPOSSIBLE":
            if total_steps == "IMPOSSIBLE":
                total_steps=int(new_steps)
            elif new_steps < total_steps:
                total_steps=int(new_steps)

    return (total_steps)
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        Hd,Ad,Hk,Ak,B,D=map(int,input().split())
        print("Case #{}: {}".format(i+1,solve(Hd,Ad,Hk,Ak,B,D)))