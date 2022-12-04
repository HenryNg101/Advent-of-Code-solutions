#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream reader("input");
    string s;
    int sum = 0, res = 0;
    while(getline(reader, s)){
        if(!s.size()){
            res = max(res, sum);
            sum = 0;
        }
        else sum += stoi(s);
    }
    res = max(res, sum);
    cout << res << endl;
    return 0;
}