#include <stdio.h>
#include <stdlib.h>
int numb(int n, int digit)
{
    int c = 0;
    while (n / 10 != 0) {
        if (n % 10 == digit) {
            c++;
            break;
        }
        n /= 10;
    }
    if (digit == n) {
        c++;
    }
    return c;
}
int main(void)
{
    int a;
    while (scanf("%d", &a) == 1) {
        int count = 0;
        int i = 0;
        while (i < 10) {
            count += numb(abs(a), i);
            ++i;
        }
        printf("%s\n", (count < 10 ? "True" : "False"));
    }
    return 0;
}
