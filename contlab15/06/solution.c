/*
сложение всех столбцов, содержащих минимальный элемент матрицы, и замена последнего из них на результат сложения
обработанная матрица
1 2 3
4 5 6
7 1 9
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
        int idx_max = 0;

        for (int j = 0; j < cur_size; ++j) {
            for (int i = 0; i < cur_size; ++i) {
                if (mas[i][j] <= min_elem) {
                    min_elem = mas[i][j];
                    idx_max = j;
                }
            }
        }
        
        for (int j = idx_max - 1; j >= 0; --j) {
            for (int i = 0; i < cur_size; ++i) {
                if (mas[i][j] == min_elem) {
                    for (int k = 0; k < cur_size; ++k) {
                        mas[k][idx_max] += mas[k][j];
                    }
                    break;
                }
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

