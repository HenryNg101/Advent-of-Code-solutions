#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream reader("input");
    string s;
    int total = 0;
    while(getline(reader, s)){
        bool low_1[26] = {false}, low_2[26] = {false}, up_1[26] = {false}, up_2[26] = {false};
        int start = 0, end = s.size() - 1;
        while(start < end){
            if(s[start] <= 'Z') up_1[s[start] - 'A'] = true;
            else low_1[s[start] - 'a'] = true;

            if(s[end] <= 'Z') up_2[s[end] - 'A'] = true;
            else low_2[s[end] - 'a'] = true;
            start++;
            end--;
        }
        for(int i=0; i<26; ++i){
            if(low_1[i] && low_2[i]) total += i + 1;
            if(up_1[i] && up_2[i]) total += i + 27;
        }
    }
    cout << total << endl;
    return 0;
}
