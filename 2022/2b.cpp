#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream reader("input");
    string s;
    int total = 0;
    //Mapping the one that a character (A, B, C) can defeats (X, Y, Z), with all cases (win, draw, lose)
    vector<vector<char>> win = {{'Z','X','Y'}, {'X','Y','Z'}, {'Y','Z','X'}};
    
    while(getline(reader, s)){
        total += (s[2] - 'X') * 3;
        total += win[s[0] - 'A'][s[2] - 'X'] - 'X' + 1;
    }
    cout << total << endl;
    return 0;
}
