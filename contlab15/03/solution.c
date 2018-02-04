/*
перестановка столбцов с максимальной и минимальной суммой элементов (с минимальными номерами соответственно)
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
        
        long long max_sum, min_sum, tmp_sum = 0, idx_min = 0, idx_max = 0;
        
        for (int i = 0; i < cur_size; ++i) {
            tmp_sum += mas[i][0];
        }
        
        min_sum = tmp_sum;
        max_sum = tmp_sum;
        
        for (int j = 1; j < cur_size; ++j) {
            tmp_sum = 0;
            for (int i = 0; i < cur_size; ++i) {
                tmp_sum += mas[i][j];
            }
            if (tmp_sum > max_sum) {
                max_sum = tmp_sum;
                idx_max = j;
            } else if (tmp_sum < min_sum) {
                min_sum = tmp_sum;
                idx_min = j;
            }
        }
        
        long long tmp_elem;
        for (int i = 0; i < cur_size; ++i) {
            tmp_elem = mas[i][idx_min];
            mas[i][idx_min] = mas[i][idx_max];
            mas[i][idx_max] = tmp_elem;
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

