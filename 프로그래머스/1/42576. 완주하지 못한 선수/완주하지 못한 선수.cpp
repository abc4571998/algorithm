#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    // 1. 참가자, 완주자 정렬
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    // 2. 완주자 만큼 돌면서 참가자에만 존재하는 것 찾음
    int i;
    for(i = 0; i < completion.size(); i++) {
        if(participant[i] != completion[i]) break;
    }
    return participant[i];
    // 3. 없으면 마지막임
}