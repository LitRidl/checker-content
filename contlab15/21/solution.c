/*
перестановка в обратном порядке элементов столбца (первого найденного), содержащего максимальный элемент матрицы
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
        
        long long max_elem = mas[0][0];
        int idx_max = 0, tmp_elem;
        
        for (int j = 0; j < cur_size; ++j) {
            for (int i = 0; i < cur_size; ++i) {
                if (mas[i][j] > max_elem) {
                    max_elem = mas[i][j];
                    idx_max = j;
                }
            }
        }
        
        for (int i = 0; i < cur_size / 2; ++i) {
            tmp_elem = mas[i][idx_max];
            mas[i][idx_max] = mas[cur_size - i - 1][idx_max];
            mas[cur_size - i - 1][idx_max] = tmp_elem;
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

