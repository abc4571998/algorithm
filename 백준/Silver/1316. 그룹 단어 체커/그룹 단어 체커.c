#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {

    int num;

    scanf("%d", &num);

    char arr[num][101];


    int count = 0;

    for (int i = 0; i < num; ++i) {
        scanf("%s", arr[i]);
        int alphabet[26] = {0,};
         count++;
        for (int j = 0; j <= 101; ++j) {
            if(arr[i][j] == '\0')
                break;
            else {
                int alpha = arr[i][j] - 'a';
                if( j == 0) {
                    alphabet[alpha]++;
                }
                else if( arr[i][j-1] == arr[i][j] ) {
                    alphabet[alpha]++;
                }
                else {
                    if(alphabet[alpha] == 0) alphabet[alpha]++;
                    else {
                        count--;
                        break;
                    }
                }
            }
        }
    }

    printf("%d", count);
    return 0;
}