#include <stdio.h>


void print(int a)
{
    if (a == 0) {
        printf("0000");
    } else if (a == 1) {
        printf("0001");
    } else if (a == 2) {
        printf("0010");
    } else if (a == 3) {
        printf("0011");
    } else if (a == 4) {
        printf("0100");
    } else if (a == 5) {
        printf("0101");
    } else if (a == 6) {
        printf("0110");
    } else if (a == 7) {
        printf("0111");
    } else if (a == 8) {
        printf("1000");
    } else if (a == 9) {
        printf("1001");
    }
}

int main(void)
{
    int x = 0;
    while (scanf("%d", &x) == 1) {
        int capacity = 1;
        if (x < 0) {
            capacity = -1;
            printf("-");
        }
        while (x / 10 / capacity) {
            capacity *= 10;
        }
        
        while (capacity) {
            print(x / capacity);
            x -= x / capacity * capacity;
            capacity /= 10;
        }
        // print(x  % 10);
        printf("\n");
    }
    return 0;
}