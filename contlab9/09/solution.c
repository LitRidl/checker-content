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
    return (mod(abs(max(i * (k + 5), j * (k + 6))) - abs(min(j * (k + 7), l * (k + 8))), 20));
}

int compute_j(int i, int j, int l, int k)
{
    return (mod((3 - sign(i - j)) * abs(min(min(i * l + 5, j * l - 3), i * j + 6)), 25) - 7);
}

int compute_l(int i, int j, int l, int k)
{
    return (mod(i, 10) + mod(j, 10) + mod(l, 10));
}


int in_area(int i, int j)
{
    return in_area_2(i, j);
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
