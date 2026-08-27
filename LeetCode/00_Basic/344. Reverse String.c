#include <stdio.h>

void reverseString(char* s, int sSize) {
    // since reversed string must be stored, using swap mechanism
    // first pointer
    int first = 0;
    // last pointer
    int last = sSize-1;
    char temp;

    while (first < last) {
        temp = s[first];
        s[first] = s[last];
        s[last] = temp;

        first++;
        last --;
    }

    for (int i = 0; i<sSize; i++) {
        printf("%c", s[i]);
    }
}
