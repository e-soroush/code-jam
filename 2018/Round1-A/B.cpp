#include<set>
#include<map>
#include<list>
#include<queue>
#include<stack>
#include<string>
#include<math.h>
#include<time.h>
#include<vector>
#include<bitset>
#include<memory>
#include<utility>
#include<fstream>
#include<stdio.h>
#include<sstream>
#include<iostream>
#include<stdlib.h>
#include<string>
#include<algorithm>
#include <numeric>
using namespace std;
long long temp[1005];
int m[1005],s[1005],p[1005];
int r,b,c;

bool checkCapacity(long long t) {
    int i=0;
    for(;i<c;++i) {
        temp[i]=std::min((long long)(m[i]),std::max(0ll,(t-p[i])/s[i]));
    }
    // descending sort
    std::sort(temp,temp+c, [](const int &left, const int &right) {return left>right;});
    long long bits=std::accumulate(temp, temp+r,0ll);
    if (bits>=b)
        return true;
    else
        return false;

}

int solve() {
    std::cin >> r >> b >> c;
    int i=0;
    for (i=0; i<c; ++i){
        std::cin >> m[i] >> s[i] >> p[i];
    }
    long long h=2e18;
    long long l=0ll;
    for(; l<=h;) {
        long long mid=(l+h)/2;
        if(checkCapacity(mid))
            h=mid-1;
        else
            l=mid+1;
    }
    std::cout << l << std::endl;
    return l;

}

int main(int argc, char *argv[])
{
    int T;
    std::cin >> T;
    for(int i=0; i<T; ++i) {
        std::cout << "Case #"<< i+1 << ": ";
    }
    return 0;
}
