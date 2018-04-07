import sys
def make_guess(a,b):
    return a+(b-a)//2+1
def solve(n,a,b):
    for i in range(n):
        guess=make_guess(a,b)
        print(guess)
        print('guess', guess,file=sys.stderr)
        result=input()
        print('result,a,b',result,a,b,file=sys.stderr)
        if result=='TOO_BIG':
            b=guess-1
        elif result=='TOO_SMALL':
            a=guess
        elif result=='CORRECT':
            break
        elif result=='WRONG_ANSWER':
            print("Wrong answer: a,b,guess", a,b,guess)
            exit()
    return n

if __name__=='__main__':
    T=int(input())
    for i in range(T):
        a,b=map(int,(input()).split())
        n=int(input())
        print('input: %d a,b,n '%i,a,b,n,file=sys.stderr)
        solve(n,a,b)


