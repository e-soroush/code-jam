#include <iostream>
#include <vector>
#include <math.h>
#include <tuple>
#include <algorithm>


int solve() {
    int n,p;
    std::cin >> n >> p;
    std::vector<int> recipe(n);
    std::vector<std::vector<int>> packages(n);
    std::vector<std::vector<std::vector<int>>> servingCount(n);
    for (int i=0; i<n; ++i){
        std::cin >> recipe[i];
    }
    for (int i=0; i<n; ++i){
        packages[i].resize(p);
        for(int j=0; j<p; ++j){
            std::cin>>packages[i][j];
        }
    }
    for (int i=0; i<n; ++i){
        servingCount[i].resize(p);
        for(int j=0; j<p; ++j){
            int minCount=floor(packages[i][j]*0.9/recipe[i]);
            int maxCount=ceil(packages[i][j]*1.1/recipe[i]);
            servingCount[i][j].push_back(minCount);
            servingCount[i][j].push_back(maxCount);
        }
    }
    std::vector<std::vector<std::vector<int>>> kits(p);
    for (int r=0; r<p; ++r){
        kits.resize(p);
        int minCount=servingCount[0][r][0];
        int maxCount=servingCount[0][r][1];
        if (minCount > maxCount)
            continue;
        for (int i=1; i<n; ++i){
            for(int j=0; j<p; ++j){
                if((minCount>=servingCount[i][j][0] && minCount<=servingCount[i][j][1]) ||
                        (maxCount>=servingCount[i][j][0] && maxCount<=servingCount[i][j][1]) ||
                        (minCount<=servingCount[i][j][0] && maxCount>=servingCount[i][j][1]))
                {
                    kits[r][j].push_back(j);
                }
            }
        }
        std::sort(kits[r].begin(),kits[r].end(),
                  [](const std::vector<int>& a,const std::vector<int>& b){return a.size()>b.size();});
    }
    int cnt=0;
    for(int i=0; i<p; ++i){
        int k=-1;
        for (int j=0; j<p; ++j){
            if(kits[i][j].size()>0){
                k=kits[i][j][0];
                cnt++;
                for(int s=0; s<p; ++s){
                    for (int ss=0; ss<kits[i][s].size(); ++ss)
                        if(kits[i][j][ss]==k)
                            kits[i][s].erase(kits[i][s].begin()+ss);
                }
                break;
            }

        }
    }
    return n;

}

int main(int argc, char *argv[])
{
    int T;
    std::cin >> T;
    for(int i=0; i<T; ++i) {
        std::cout << "Case #"<<i+1<<": " << solve() << std::endl;
    }
    return 0;
}
