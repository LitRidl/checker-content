/*
замена всех столбцов, содержащих минимальный элемент матрицы, на столбец с максимальным номером, содержащий ее максимальный элемент
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
        long long max_elem = mas[0][0], min_elem = mas[0][0], max_column = 0;

        for (int j = 0; j < cur_size; ++j) {
            for (int i = 0; i < cur_size; ++i) {
                if (mas[i][j] >= max_elem) {
                    max_elem = mas[i][j];
                    max_column = j;
                } else if (mas[i][j] < min_elem) {
                    min_elem = mas[i][j];
                }
            }
        }

        for (int i = 0; i < cur_size; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                if(mas[i][j] == min_elem) {
                    for(int k = 0; k < cur_size; ++k) {
                        mas[k][j]= mas[k][max_column];
                    }
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

