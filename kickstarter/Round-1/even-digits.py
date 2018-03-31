from math import log10, ceil,pow


def get_eights(num_digits):
    n=0
    for i in range(num_digits+1):
       n+=8*pow(10,i)
    return n 

def button_presses(n):
    count=0
    # num_digits=ceil(log10(n+0.1))
    number=list(map(int,list(str(n))))
    num_digits=len(number)
    for i in (range(num_digits)):
        digit=number[i]
        if digit%2==1:
            if digit!=9:
                t1=pow(10,num_digits-i-1)*(digit+1)
            else:
                t1=pow(10,num_digits-i)*2
            if digit!=1:
                t2=pow(10,num_digits-i-1)*(digit-1)+get_eights(num_digits-i-2)
            else:
                t2=get_eights(num_digits-i-2)
            # num=n%pow(10,num_digits-i)
            num=0
            for j in range(i,num_digits):
                num+=int(number[j]*pow(10,num_digits-j-1))
            # num=int(num)
            t1=int(t1)
            t2=int(t2)
            if num-t2>t1-num: # add
                count+=t1-num
                n+=t1-num
            else: # subtract
                count+=num-t2
                n-=num-t2
            n=int(n)
            break
    num_digits=ceil(log10(n+0.1))
    number=list(map(int,list(str(n))))
    for i in range(num_digits):
        if number[i]%2 !=0:
            print(n)

    return int(count)


def test_res():
    n=10000000000000000
    print('n, r', n, button_presses(n))

if __name__=='__main__':
    # test_res()
    T=int(input())
    for i in range(T):
        n=int(input())
        print('Case #%d: %d'%(i+1,button_presses(n)))