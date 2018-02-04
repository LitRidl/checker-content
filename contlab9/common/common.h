#ifndef __COMMON_H_
#define __COMMON_H_

#include <math.h>

int min(int x, int y)
{
    return (x < y) ? x : y;
}

int max(int x, int y)
{
    return (x > y) ? x : y;
}

int sign(int x)
{
    return (x > 0) - (x < 0);
}

int mod(int a, int b)
{
    return abs(((a % b) + b) % b);
}

int _mod(int a, int b)
{
    if (b < 0) {
        return mod(a, -b);
    }
    int res = a % b;
    if (res < 0) {
        res += b;
    }
    return res;
}

int _div(int a, int b)
{
    return floor(1.0 * a / b);
}

#endif
