#include <stdio.h>

/*capacity 100000 678273
a = 678273 / 100000
b = 678273 % 10
678273 - (a - b) * capacity + (a - b)
x += -(a - b) * (1 - capacity);
*/

long long capacity(long long x)
{
    long long c = 1;
    while (x) {
        x /= 10;
        c *= 10;
    }
    return c / 10;
}

int first_number(long long x)
{
    return x / capacity(x);
}

int last_number(long long x)
{
    return x % 10;
}

int main(void)
{
    long long x;
    while ((scanf("%lld", &x)) == 1) {
        if (x) {
            x += -1 * (first_number(x) - last_number(x)) * capacity(x) + (first_number(x) - last_number(x));
            printf("%lld\n", x);
        } else {
            printf("%lld\n", x);
        }
    }
    return 0;
}
