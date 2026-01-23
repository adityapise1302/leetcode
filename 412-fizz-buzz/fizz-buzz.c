/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
char** fizzBuzz(int n, int* returnSize) {
    char** answer = malloc(sizeof(char*) * n);
    *returnSize = n;
    for(int i = 1; i <= n; i++) {
        answer[i - 1] = malloc(sizeof(char)*12);
        if(i%3 == 0 && i%5 == 0) {
            strcpy(answer[i-1], "FizzBuzz");
        } else if (i % 3 == 0) {
            strcpy(answer[i-1], "Fizz");
        } else if (i % 5 == 0) {
            strcpy(answer[i-1], "Buzz");
        } else {
            sprintf(answer[i-1], "%d", i);
        }
    }
    return answer;
}
