//43 of 48 test cases
#include <stdio.h>
#include <stdlib.h>

int* dailyTemperatures(int* temperatures, int temperaturesSize, int* returnSize) {
    int* june = (int*)malloc(sizeof(int) * temperaturesSize);
    *returnSize = temperaturesSize;

    for (int i = 0; i < temperaturesSize; i++) {
        june[i] = 0;  // Initialize the june array to zero

        for (int j = i + 1; j < temperaturesSize; j++) {
            if (temperatures[j] > temperatures[i]) {
                june[i] = j - i;
                break;  // Break the j loop when a higher temperature is found
            }
        }
    }

    return june;
}

