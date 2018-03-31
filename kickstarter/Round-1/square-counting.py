import sys
from tqdm import tqdm
MOD=1e9+7
def find_squares(r,c):
    m=int(min(r,c))
    rc=int(((r%MOD)*(c%MOD))%MOD)
    mm2=int(((m/2*(m-1)))%MOD)
    # mm3=int((m*(m-1)//2)%MOD)
    # assert mm2==mm3
    total=int(int((rc*mm2)%MOD)+(int((mm2*mm2)%MOD)-int((int((r+c)%MOD)*int((((m-1)*m/2*(2*m-1)/3))%MOD))))%MOD)
    total%=MOD
    return int(total)


def test_alg():
    r,c=1000,500
    print('r,c total square: ', r,c,find_squares(r,c))

if __name__=='__main__':
    # test_alg()
    # print(sys.argv)
    n=int(input())
    for i in tqdm(range(n)):
        r,c = map(int,(input().split()))
        print("Case #%d: %d"%(i+1,find_squares(r,c)))
        