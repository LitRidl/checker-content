/*
циклический сдвиг элементов матрицы по спирали против часовой стрелки на n элементов (n задается со стандарного потока ввода)
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
    
    long long mas[max_size * max_size];
    
    for (int test = 0; test < tests; ++test) {
        scanf("%d", &cur_size);
        for (int i = 0; i < cur_size * cur_size; ++i) {
                scanf("%lld", &(mas[i]));
        }
        
        long long tmp = 0;
        for (int k = 0; k < shift; ++k) {
            tmp = mas[0];
            for(int i = 0; i < (cur_size * cur_size - 1); ++i) {
                mas[i] = mas[i + 1];
            }
            mas[cur_size * cur_size - 1] = tmp;
        }
        
        if(cur_size > 0) {
            for (int i = cur_size; i <= cur_size * cur_size; i += cur_size) {
                for(int j = cur_size; j > 0; --j) {
                    printf("%lld ", mas[i - j]);
                }
                printf("\n");
            }
        }
    }
    
    return 0;
}
