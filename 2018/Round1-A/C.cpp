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
#include <iomanip>

# define sqr(x) (double(x*x))
# define vvi std::vector<std::vector<double>>
# define vi std::vector<double>







int n,p;
int w[100],h[100];

void solve() {
    std::cin >> n >> p;
    double perimter=0;
    vvi s(n, vi(2,-1.0));
    for(int i=0; i<n; ++i){
        std::cin >> w[i] >> h[i];
        perimter+=2*(w[i]+h[i]);
        s[i][0]=2*(std::min(w[i], h[i]));
        s[i][1]=2*(sqrt(sqr(w[i])+sqr(h[i])));
    }
    p-=perimter;
    vvi space;
    for (int i=0; i<s.size(); ++i){
        double low=s[i][0];
        double high=s[i][1];
        int s_size=space.size();
        vvi space_tmp = space;
        for (int j=0; j<space.size(); ++j){
            double tempLow=low+space[j][0];
            if (tempLow>p)
                continue;
            double tempHigh=high+space[j][1];
            bool merged=false;
            for (int k=0; k<s_size; ++k){
                if(tempLow<=space[k][0] && tempHigh>=space[k][0]){
                    space_tmp[k][0]=tempLow;
                    space_tmp[k][1]=std::max(tempHigh, space[k][1]);
                    merged=true;
                    break;
                }
            }
            if(merged==false) {
                vi tmp(2);
                tmp[0]=tempLow;
                tmp[1]=tempHigh;
                space_tmp.push_back(tmp);
            }
        }
        space = space_tmp;
        if (low <= p){
            vi tmp(2);
            tmp[0]=low;
            tmp[1]=high;
            space.push_back(tmp);
        }
    }
    double maxH=0.0;
    for(int i=0; i<space.size(); ++i){
        if(maxH<space[i][1])
            maxH=space[i][1];
    }
    if(maxH>p)
        std::cout << std::fixed << std::setprecision(6) << double(perimter+p) <<std::endl;
    else
        std::cout << std::fixed << std::setprecision(6) << double(perimter+maxH) << std::endl;
}

int main(int argc, char *argv[])
{
    int T;
    std::cin >> T;
    for(int i=1; i<=T; ++i) {
        std::cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}
