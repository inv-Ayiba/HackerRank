#include <stdlib.h>

int* dailyTemperatures(int* temperatures, int temperaturesSize, int* returnSize) {
    int* result = (int*)malloc(sizeof(int) * temperaturesSize);  // Allocate memory for the result array
    *returnSize = temperaturesSize;

    // Stack to store indices of temperatures
    int stack[temperaturesSize];
    int top = -1;

    for (int i = 0; i < temperaturesSize; i++) {
        while (top != -1 && temperatures[i] > temperatures[stack[top]]) {
            // Pop elements from the stack and update the result array
            int index = stack[top--];
            result[index] = i - index;
        }
        // Push the current index onto the stack
        stack[++top] = i;
    }

    // For days with no higher temperature, result is 0
    while (top != -1) {
        result[stack[top--]] = 0;
    }

    return result;
}
