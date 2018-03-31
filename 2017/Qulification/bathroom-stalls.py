import os
import numpy as np
import math
import time

from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def read_input(path):
    with open(path) as fhandler:
        number_of_instances=int(fhandler.readline().strip())
        instances = [(int(l.split()[0]), int(l.split()[1])) for l in fhandler.readlines()]
    return number_of_instances,instances


def get_last_state(instance):
    """
    Allocate each people to the farthest empty stalls.
    For small samples this function works, however, for small part 2 and
    large sample we should call `partition_peoples` 
    """
    empty,people = instance[0], instance[1]
    occupied=np.array([0,(1+people)])
    for _ in range(people):
        empty_stalls_between=occupied[1:]-occupied[:-1]
        most_distan_index=empty_stalls_between.argmax()
        lef_most_distance=(occupied[most_distan_index+1]-occupied[most_distan_index])//2+occupied[most_distan_index]
        occupied=np.sort(np.append(occupied,lef_most_distance))
    most_distan_index=np.where(occupied==lef_most_distance)[0][0]
    ls=occupied[most_distan_index]-occupied[most_distan_index-1]-1
    rs=occupied[most_distan_index+1]-occupied[most_distan_index]-1

    return max(ls,rs), min(ls,rs)
    

def partition_peoples(instance):
    """
    For large samples we should recursivey partition peoples with partitioning peoples in 
    empty stalls by half. For odd peoples, we should assign one empty stall to one person and 
    partition remaining even peoples to empty stalls 
    """
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
    return partition_peoples((empty,people))




if __name__ == '__main__':
    data_path = os.path.join(os.path.dirname(__file__), 'C-large-practice.in')
    number_of_instances,instances=read_input(data_path)
    print('number of instances %d'%number_of_instances)
    result=[None]*number_of_instances
    for i,instance in enumerate(instances):
        result[i]=partition_peoples(instance)
        print(instance,result[i])
    
    with open(data_path+'.result', 'w') as fhandler:
        fhandler.writelines('\n'.join(['Case #%d: %d %d'%(i+1,m1, m2)  for i,(m1,m2) in enumerate(result)]))