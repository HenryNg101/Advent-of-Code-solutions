#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream reader("input");
    string s1, s2, s3;
    int total = 0;
    while(getline(reader, s1)){
        getline(reader, s2);
        getline(reader, s3);
        bool check1[52] = {false}, check2[52] = {false}, check3[52] = {false};
        for(auto e: s1){
            if (e <= 'Z') check1[e - 'A' + 26] = true;
            else check1[e - 'a'] = true;
        }
        for(auto e: s2){
            if (e <= 'Z') check2[e - 'A' + 26] = true;
            else check2[e - 'a'] = true;
        }
        for(auto e: s3){
            if (e <= 'Z') check3[e - 'A' + 26] = true;
            else check3[e - 'a'] = true;
        }
        for(int i=0; i<52; ++i){
            if(check1[i] && check2[i] && check3[i]) total += i + 1;
        }
    }
    cout << total << endl;
    return 0;
}
