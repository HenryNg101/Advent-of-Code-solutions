#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream reader("input");
    string s;
    int sum = 0;
    vector<int> v;
    while(getline(reader, s)){
        if(!s.size()){
            v.push_back(sum);
            sum = 0;
        }
        else sum += stoi(s);
    }
    v.push_back(sum);
    sort(v.begin(), v.end(), greater<int>());
    cout << v[0] + v[1] + v[2] << endl;
    return 0;
}