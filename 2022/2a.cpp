#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream reader("input");
    string s;
    int total = 0;
    //Mapping the one that a character (A, B, C) can defeats (X, Y, Z)
    unordered_map<char, char> win = {{'A', 'Z'}, {'B', 'X'}, {'C', 'Y'}};
    
    while(getline(reader, s)){
        total += s[2] - 'X' + 1;
        if((s[0] - 'A') == (s[2] - 'X')) total += 3;
        else total += (win[s[0]] == (s[2])) ? 0 : 6;
    }
    cout << total << endl;
    return 0;
}
