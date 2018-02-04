#include <math.h>

// lines i + j + 10 = 0, i + j + 20 = 0
#define L_UPPER  -10
#define L_LOWER  -20


int in_area_4(int x, int y)
{
    return (x + y) >= L_LOWER && (x + y) <= L_UPPER;
}
