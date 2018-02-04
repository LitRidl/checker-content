/*
циклический сдвиг элементов матрицы в столбцовом представлении на n элементов (n задается со стандарного потока ввода)
обработанная матрица
1 2 3
4 5 6
7 8 9
*/
#include <stdio.h>

int main(void)
{
    int tests, max_size, cur_size, shift;
    scanf("%d%d%d", &tests, &max_size, &shift);
    
    long long mas[max_size][max_size];
    
    for (int test = 0; test < tests; ++test) {
        scanf("%d", &cur_size);
        for (int i = 0; i < cur_size; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                scanf("%lld", &(mas[i][j]));
            }
        }
        
        for (int i = 0; i < cur_size; ++i) {
            for(int k = 0; k < shift; ++k) {
                long long tmp = mas[i][cur_size - 1];
                for (int j = 0; j < cur_size - 1; ++j) {
                    mas[i][cur_size - 1 - j] = mas[i][cur_size - 1 - j - 1];
                }
                mas[i][0] = tmp;
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
