/*
перестановка строк с максимальным и минимальным произведением элементов (с максимальными номерами соответственно)
обработанная матрица
1 2 3
4 5 6
7 8 9
*/
#include <stdio.h>

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
        
        long long max_mul = 1, min_mul = 1, tmp_mul = 1, idx_min = 0, idx_max = 0;
        
        for (int j = 0; j < cur_size; ++j) {
            tmp_mul *= mas[0][j];
        }
        
        min_mul = tmp_mul;
        max_mul = tmp_mul;
        
        for (int i = 1; i < cur_size; ++i) {
            tmp_mul = 1;
            for (int j = 0; j < cur_size; ++j) {
                tmp_mul *= mas[i][j];
            }
            if (tmp_mul >= max_mul) {
                max_mul = tmp_mul;
                idx_max = i;
            }
            if (tmp_mul <= min_mul) {
                min_mul = tmp_mul;
                idx_min = i;
            }
        }
        
        long long tmp_elem;
        for (int j = 0; j < cur_size; ++j) {
            tmp_elem = mas[idx_min][j];
            mas[idx_min][j] = mas[idx_max][j];
            mas[idx_max][j] = tmp_elem;
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

