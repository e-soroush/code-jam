#include <iostream>
#include <vector>
#include <map>
#include <numeric>


std::map<char,int> plate_map = {
    {'@',1},
    {'.',0}
};

int sum_vertical(std::vector<std::vector<int>> plate,int col, int sp=-1) {
    int s=0;
    int b = sp > 0 ? sp : plate.size();
    for(int i=0; i<b; ++i) {
        s+=plate[i][col];
    }
    return s;
}
std::string solve() {
    int r,c,h,v;
    std::cin >> r>>c>>h>>v;
    char in;
    int total_chocolate=0;
    std::vector<std::vector<int>> plate(r);
    for(int i=0; i<r; ++i){
        plate[i].resize(c);
        for(int j=0; j<c; ++j) {
            std::cin >> in;
            plate[i][j]=plate_map[in];
            total_chocolate+=plate_map[in];
        }
    }

    int chocolate_each_person=total_chocolate/((h+1)*(v+1));
    if(chocolate_each_person*((h+1)*(v+1))!=total_chocolate)
        return "IMPOSSIBLE";
    int chocolate_each_col=chocolate_each_person*(h+1);
    int chocolate_each_row=chocolate_each_person*(v+1);
    std::vector<int> cut_h;
    int tmp=0;

    for(int i=0; i<r; ++i){
        tmp+=std::accumulate(plate[i].begin(),plate[i].end(),0);
        if(tmp==chocolate_each_row){
            tmp=0;
            cut_h.push_back(i);
        }
    }
    int base=0;
    for(int i=0; i<c; ++i){
        tmp+=sum_vertical(plate,i);
        if(tmp==chocolate_each_col){
            tmp=0;
            int b=0;
            for(int j=0; j<cut_h.size(); ++j){
                for(int k=0; k<(cut_h[j]-b)+1; ++k){
                    tmp+=std::accumulate(plate[b+k].begin()+base,plate[b+k].begin()+i+1,0);
                }
                if(tmp!=chocolate_each_person)
                    return "IMPOSSIBLE";
                tmp=0;
                b=cut_h[j]+1;
            }
        base=i+1;
        } else if(tmp > chocolate_each_col)
            return "IMPOSSIBLE";
    }
    return "POSSIBLE";


}

int main(int argc, char** argv) {
    int T;
    std::cin >> T;
    for (int i =0; i<T; ++i){
        std::cout << "Case #" << i+1 << ": "<< solve()<<std::endl;
    }
}
