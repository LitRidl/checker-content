/*
удаление всех строк, содержащих минимальный элемент матриц
обработанная матрица
1 2 3
4 5 1
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
        long long min_elem = mas[0][0];
        
        for (int i = 0; i < cur_size; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                if (mas[i][j] < min_elem) {
                    min_elem = mas[i][j];
                }
            }
        }
        
        int cnt_min_elem = 0;
        
        for (int i = 0; i < cur_size - cnt_min_elem; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                if (mas[i][j] == min_elem) {
                    ++cnt_min_elem;
                    for (int tmp_i = i; tmp_i < cur_size - cnt_min_elem; ++tmp_i) {
                        for (int tmp_j = 0; tmp_j < cur_size; ++tmp_j) {
                            mas[tmp_i][tmp_j] = mas[tmp_i + 1][tmp_j];
                        }
                    }
                    --i;
                    break;
                }
            }
        }
        
        
        for (int i = 0; i < cur_size - cnt_min_elem; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                printf("%lld ", mas[i][j]);
            }
            printf("\n");
        }
    }
    
    
    
    return 0;
}

