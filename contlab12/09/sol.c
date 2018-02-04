#include <stdio.h>
#include <stdlib.h>
 
int compute_number(int k)
{
    int number = k;
    int last = 9;
    if (number < 0) {
        number = number * (-1);
    }
    if (number == 0) {
        return 0;
    }
    while (number != 0) {
        int s = number % 10;
        if (s > last) {
            return 1;
        }

        last = s;
        number = number / 10;
    }
    return 0;
}

int main(void)
{
    int n;
    while (scanf("%d", &n) == 1) {
        (compute_number(n) == 1) ? printf("False\n") : printf("True\n");
    }

    return 0;
}

