/*
удаление повторяющихся столбцов матрицы (оставить только первый из них)
обработанная матрица
1 2 2
4 5 5
7 8 8
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
        
        int cnt_same = 0;
        
        for (int j = 0; j < cur_size - cnt_same; ++j) {
            for (int j_next = j + 1; j_next < cur_size - cnt_same; ++j_next) {
                for (int i = 0; i < cur_size; ++i) {
                    if (mas[i][j] != mas[i][j_next]) {
                        break;
                    }
                    if (i == cur_size - 1) {
                        ++cnt_same;
                        for (int tmp_j = j_next; tmp_j < cur_size - cnt_same; ++tmp_j) {
                            for (int tmp_i = 0; tmp_i < cur_size; ++tmp_i) {
                                mas[tmp_i][tmp_j] = mas[tmp_i][tmp_j + 1];
                            }
                        }
                        --j_next;
                    }
                    
                }
            }
        }
        
        
        for (int i = 0; i < cur_size ; ++i) {
            for (int j = 0; j < cur_size - cnt_same; ++j) {
                printf("%lld ", mas[i][j]);
            }
            if (cur_size - cnt_same) {
                printf("\n");
            }
        }
    }
    
    return 0;
}

