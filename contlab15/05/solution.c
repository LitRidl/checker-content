/*
сложение всех строк, содержащих максимальный элемент матрицы, и замена первой из них на результат сложения
обработанная матрица
1 9 3
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
        int idx_max = 0;
        
        for (int i = 0; i < cur_size; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                if (mas[i][j] > max_elem) {
                    max_elem = mas[i][j];
                    idx_max = i;
                }
            }
        }
        
        for (int i = idx_max + 1; i < cur_size; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                if (mas[i][j] == max_elem) {
                    for (int k = 0; k < cur_size; ++k) {
                        mas[idx_max][k] += mas[i][k];
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

