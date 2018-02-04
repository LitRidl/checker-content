/*
удаление всех строк, содержащих максимальный элемент матриц
целое число
1 2 3
4 5 9
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
        
        for (int i = 0; i < cur_size; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                if (mas[i][j] > max_elem) {
                    max_elem = mas[i][j];
                }
            }
        }
        
        int cnt_max_elem = 0;
        
        for (int j = 0; j < cur_size - cnt_max_elem; ++j) {
            for (int i = 0; i < cur_size; ++i) {
                if (mas[i][j] == max_elem) {
                    ++cnt_max_elem;
                    for (int tmp_j = j; tmp_j < cur_size - cnt_max_elem; ++tmp_j) {
                        for (int tmp_i = 0; tmp_i < cur_size; ++tmp_i) {
                            mas[tmp_i][tmp_j] = mas[tmp_i][tmp_j + 1];
                        }
                    }
                    --j;
                    break;
                }
            }
        }
        
        
        for (int i = 0; i < cur_size ; ++i) {
            for (int j = 0; j < cur_size - cnt_max_elem; ++j) {
                printf("%lld ", mas[i][j]);
            }
            if (cur_size - cnt_max_elem) {
                printf("\n");
            }
        }
    }
    
    return 0;
}

