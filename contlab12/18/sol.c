#include <stdio.h>

int getCapacity(int num)
{
    int a = 1;
    while (num / a / 100) {
        a *= 10;
    }
    return a;
}

long long f(int num)
{
    long long res = num;
    int capacity = getCapacity(res);
    res += res / 10 % 10 * capacity + res / capacity % 10 * 10 - res % 100 / 10 * 10 - res / capacity % 10 * capacity;
    return res;
}

int main(void)
{
    int num;
    while (scanf("%d", &num) == 1) {
        if (num > 1000 || num < -1000) {
            long long res = f(num);
            printf("%lld\n", res);
        } else {
            printf("%d\n", num);
        }
    }
    return 0;
}
