/*
замена всех минимальных элементов матрицы на число строк, содержащих её максимальный элемент
обработанная матрица
1 2 9
9 1 1
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
        long long max_elem = mas[0][0], min_elem = mas[0][0], cnt_max_elem = 0;
        
        for (int i = 0; i < cur_size; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                if (mas[i][j] > max_elem) {
                    max_elem = mas[i][j];
                    cnt_max_elem = 1;
                    break;
                } else if (mas[i][j] < min_elem) {
                    min_elem = mas[i][j];
                } else if (mas[i][j] == max_elem) {
                    ++cnt_max_elem;
                }
            }
        }
        
        for (int i = 0; i < cur_size; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                if (mas[i][j] == min_elem) {
                    mas[i][j] = cnt_max_elem;
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

