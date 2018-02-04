/*
замена элементов побочной диагонали суммами элементо, проходящих через них главной и других параллельных диагоналей
обработанная матрица
1 2 3
4 5 6
7 8 9
*/

#include <stdio.h>

int min(int a, int b)
{
    return a < b ? a : b;
}

int main(void)
{
    int tests, max_size, cur_size;
    scanf("%d%d", &tests, &max_size);
    
    long long mas[max_size][max_size];
    int test;
    int i, j;
    for (test = 0; test < tests; ++test) {
        scanf("%d", &cur_size);
        for (i = 0; i < cur_size; ++i) {
            for (j = 0; j < cur_size; ++j) {
                scanf("%lld", &(mas[i][j]));
            }
        }
        j = 0;
        int k;
        for(i = cur_size - 1; i >= 0; i--) {
            int ix = i - 1, jx = j - 1;
            while(ix >= 0 && jx >= 0) {
                mas[i][j] += mas[ix][jx];
                ix -= 1;
                jx -= 1;
            }
            ix = i + 1, jx = j + 1;

            while(ix <= cur_size-1 && jx <= cur_size-1) {
                mas[i][j] += mas[ix][jx];
                ix += 1;
                jx += 1;
            }
            j++;
        }

        for (i = 0; i < cur_size; ++i) {
            for (j = 0; j < cur_size; ++j) {
                printf("%lld ", mas[i][j]);
            }
            printf("\n");
        }
    }
    
    return 0;
}

