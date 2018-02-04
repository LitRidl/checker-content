/*
умножение строки с минимальным элементом матрицы на столбец с максимальным элементом
целое число
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
        
        long long max_elem = mas[0][0], min_elem = mas[0][0], max_idx = 0, min_idx = 0;
        
        for (int i = 0; i < cur_size; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                if (mas[i][j] > max_elem) {
                    max_elem = mas[i][j];
                    max_idx = j;
                } else if (mas[i][j] == max_elem && j < max_idx) {
                    max_idx = j;
                }
                
                if (mas[i][j] < min_elem) {
                    min_elem = mas[i][j];
                    min_idx = i;
                } else if (mas[i][j] == min_elem && i < min_idx) {
                    min_idx = i;
                }
            }
        }
        
        long long res = 0;
        
        for (int i = 0; i < cur_size; ++i) {
            res += mas[min_idx][i] * mas[i][max_idx];
        }
        
        printf("%lld\n", res);
    }
    
    return 0;
}

