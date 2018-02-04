/*
замена элементов главной диагонали суммами элементов, проходящих через них побочных диагоналей
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
    
    for (int test = 0; test < tests; ++test) {
        scanf("%d", &cur_size);
        for (int i = 0; i < cur_size; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                scanf("%lld", &(mas[i][j]));
            }
        }
        
        for (int i = 0; i < cur_size; ++i) {
            for (int j = 0; j < min(i, cur_size - i - 1); ++j) {
                mas[i][i] += mas[i + j + 1][i - j - 1];
                mas[i][i] += mas[i - j - 1][i + j + 1];
            }
        }
        
        for (int i = 0; i < cur_size; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                printf("%lld ", mas[i][j]);
            }
            printf("\n");
        }
    }
    
    return 0;
}

