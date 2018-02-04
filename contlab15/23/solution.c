/*
нахождение суммы элементов строки с минимальным номером, содержащей максимальный элемент матрицы
целое число
1 2 5
4 9 6
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
        
        long long sum = 0;
        
        for (int j = 0; j < cur_size; ++j) {
            sum += mas[idx_max][j];
        }
        
        printf("%lld\n", sum);
        
    }
    
    return 0;
}

