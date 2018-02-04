/*
удаление повторяющихся строк матрицы (оставить только первую из них)
обработанная матрица
1 2 3
4 5 6
4 5 6
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

        for(int i = 0; i < cur_size - cnt_same; ++i) {
            for(int i_next = i + 1; i_next < cur_size - cnt_same; ++i_next) {
                for(int j = 0; j < cur_size; ++j) {
                    if(mas[i][j] != mas[i_next][j])
                        break;
                    if(j == cur_size - 1) {
                        ++cnt_same;
                        for (int tmp_i = i_next; tmp_i < cur_size - cnt_same; ++tmp_i) {
                            for (int tmp_j = 0; tmp_j < cur_size; ++tmp_j) {
                                mas[tmp_i][tmp_j] = mas[tmp_i + 1][tmp_j];
                            }
                        }
                        --i_next;
                    }
                }
            }
        }
        
        
        for (int i = 0; i < cur_size - cnt_same; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                printf("%lld ", mas[i][j]);
            }
            printf("\n");
        }
    }
    
    return 0;
}

