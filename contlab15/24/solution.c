/*
нахождение произведения элементов столбца с максимальным номером, содержащим минимальный элемент матрицы
целое число
1 2 5
4 1 6
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
        
        long long mult = 1;
        
        for (int i = 0; i < cur_size; ++i) {
            mult *= mas[i][idx_max];
        }
        
        cur_size == 0 ? printf("0\n") : printf("%lld\n", mult);
        
    }
    
    return 0;
}

