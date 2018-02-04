#include <stdio.h>
#include <stdlib.h>

long long add_one(long long input)
{
    long long compacity = 10;
    while (input / compacity) {
        compacity *= 10;
    }
    if (input < 0) {
        input -= compacity;
        input = input * 10 - 1;
    } else {
        input += compacity;
        input = input * 10 + 1;
    }
    return (input);
}

int main(void)
{
    int input = 0;
    while (scanf("%d", &input) == 1) {
        printf("%lli\n", add_one(input));
    }
    return 0;
}
