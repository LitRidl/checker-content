#include<stdio.h>

int even_parity(int n)
{
    int k, position_shift = 1;
    for (k = 0; n; n /= 10) {
        if ((n % 10) % 2) {
            k += (n % 10) * position_shift;
            position_shift *= 10;
        }
    }
    return k;
}
int main(void)
{
    int n;
    while (scanf("%d", &n) == 1) {
        printf("%d\n", even_parity(n));
    }
    return 0;
}
