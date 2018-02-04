#include <stdlib.h>

#include <stdio.h>
#include <math.h>

#include "../common/common.h"
#include "../common/var1.h"
#include "../common/var2.h"
#include "../common/var3.h"
#include "../common/var4.h"
#include "../common/var5.h"


#define K_START 1
#define K_MAX  50


int compute_i(int i, int j, int l, int k)
{
    return (mod(_div(i * i, abs(j - l) + k + 1) - _div(j * j, abs(i - l) + k + 1), 30));
}

int compute_j(int i, int j, int l, int k)
{
    return (sign(l) * min(i, j) - sign(j) * max(i, l) + k);
}

int compute_l(int i, int j, int l, int k)
{
    return (mod((i - j) * (j - l) * (l - i), 20));
}


int in_area(int i, int j)
{
    return in_area_5(i, j);
}


int main(void)
{
    int i, j, l, k;
    scanf("%d%d%d", &i, &j, &l);

    for (k = K_START - 1; !in_area(i, j) && k < K_MAX; ++k) {
        int i_old = i, j_old = j, l_old = l;

        i = compute_i(i_old, j_old, l_old, k);
        j = compute_j(i_old, j_old, l_old, k);
        l = compute_l(i_old, j_old, l_old, k);
    }

    printf("%s\n", in_area(i, j)? "Yes" : "No");
    printf("%d %d %d %d\n", i, j, l, k);

    return 0;
}