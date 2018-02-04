/*
замена всех минимальных элементов матрицы на сумму элементов соответствующего столбца
обработанная матрица
1 2 3
4 5 6
7 8 9
*/
#include <stdio.h>
#include <stdbool.h>

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
        long long min_elem = mas[0][0], row_sum = 0;
        bool first_in_column = true;
        
        for (int i = 0; i < cur_size; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                if (mas[i][j] < min_elem) {
                    min_elem = mas[i][j];
                }
            }
        }

        for (int j = 0; j < cur_size; ++j) {
            for (int i = 0; i < cur_size; ++i) {
                if(mas[i][j] == min_elem) {
                    if(first_in_column) {
                        for(int k = 0; k < cur_size; ++k) {
                            row_sum += mas[k][j];
                            first_in_column = false;
                        }
                    }
                    mas[i][j] = row_sum;
                }
            }
            first_in_column = true;
            row_sum = 0;
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
