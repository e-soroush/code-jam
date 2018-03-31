import os
import re
import numpy as np

def read_input(path):
    with open(path) as fhandler:
        number_of_instances=int(fhandler.readline().strip())
        instances = [(l.split()[0], int(l.split()[1])) for l in fhandler.readlines()]
    return number_of_instances,instances

def get_minimum_flips(instance):
    happy=0
    blank=1
    k=instance[1]
    pancake=[int(p) for p in instance[0].replace('+', str(happy)).replace('-', str(blank))]
    pancake_length = len(pancake)
    flip_count=0
    for i in range(pancake_length-1, k-2, -1):
        if pancake[i] == blank:
            flip_count+=1
            for j in range(k):
                pancake[i-j] =(pancake[i-j]+1)%2
    if sum(pancake) != 0:
        return -1
    else:
        return flip_count




if __name__ == '__main__':
    data_path = os.path.join(os.path.dirname(__file__), 'A-large-practice.in')
    number_of_instances,instances=read_input(data_path)
    print('number of inputs: %d'%number_of_instances)
    print('first two samples are ', instances[:2])
    results=-1*np.ones(len(instances))
    for i,instance in enumerate(instances):
        results[i]=get_minimum_flips(instance)
        print('flip count for {} is {}'.format(instance, results[i]))
    
    with open(data_path+'.result', 'w') as fhandler:
        fhandler.writelines('\n'.join(['Case #%d: %s'%(i+1,str(int(c)) if c!=-1 else 'IMPOSSIBLE') for i,c in enumerate(results)]))

    

