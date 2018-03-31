import os
from math import pow



def read_input(path):
    with open(path) as fhandler:
        number_of_instances=int(fhandler.readline().strip())
        instances = [l.strip() for l in fhandler.readlines()]
    return number_of_instances,instances


def __get_digits(number):
    return [int(p) for p in number]

def tidy_number(instance):
    digits=__get_digits(instance)
    for i in range(len(digits)-1, 0, -1):
        if digits[i] < digits[i-1]:
            digits[i-1] -= 1
            for j in range(len(digits)-i):
                digits[i+j]=9
    number = int(''.join([str(s) for s in digits]))
    if digits != sorted(digits):
        print('incorrect', instance, number)
    return number



if __name__ == '__main__':
    data_path = os.path.join(os.path.dirname(__file__), 'B-small-practice.in')
    number_of_instances,instances=read_input(data_path)
    print('number of instances id %d'%number_of_instances)
    results = [-1] * len(instances)
    for i,instance in enumerate(instances):
        results[i] = tidy_number(instance)
        # print('result for instance {} is {} id {}'.format(instance, results[i], i))
    
    with open(data_path+'.result', 'w') as fhandler:
        fhandler.writelines('\n'.join(['Case #%d: %s'%(i+1,c) for i,c in enumerate(results)]))
