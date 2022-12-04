#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream reader("input");
    int counter = 0;
    string s;
    while(getline(reader, s)){
        vector<int> v;
        int c = 0;
        for(auto e: s){
            if(e >= '0' && e <= '9') c = c*10 + (e - '0');
            else {
                v.push_back(c);
                c = 0;
            }
        }
        v.push_back(c);
        //Check if a head of a range is smaller than head of another range, and tail of this range greater than other range
        //Need 2 checks (range 1 contains range 2, or the other way)
        if((v[2] <= v[0] && v[3] >= v[1]) || (v[0] <= v[2] && v[1] >= v[3])) counter++;
    }
    cout << counter << endl;
    return 0;
}
