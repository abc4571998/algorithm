#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    // 1. 길이 정렬
    sort(phone_book.begin(), phone_book.end());
    // 2. 앞번호가 뒷번호의 접두어인지 확인
    for(int i = 0; i < phone_book.size() - 1; i++) {
        if(phone_book[i+1].find(phone_book[i]) == 0) return false;
    }
    return answer;
}