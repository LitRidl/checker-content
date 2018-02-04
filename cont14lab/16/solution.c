/*
4   5 11 15
10  3  6 12
14  9  2  7
16 13  8  1
*/
#include <stdio.h>

int max(int a, int b)
{
    return a > b ? a : b;
}

int min(int a, int b)
{
    return a < b ? a : b;
}

int main(void)
{
    int tests, max_size, cur_size, diag_size, way;
    scanf("%d%d", &tests, &max_size);
    
    int row, column;
    
    int mas[max_size][max_size];
    int res[max_size][max_size];
    
    for (int test = 0; test < tests; ++test) {
        scanf("%d", &cur_size);
        for (int i = 0; i < cur_size; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                scanf("%d", &(mas[i][j]));
            }
        }

        way = -1;
        
        for (int diag = 0; diag + 1 < 2 * cur_size; ++diag) {
            diag_size = cur_size - (diag + 1) / 2;
            
            if (diag % 2 == 0) {
                row = 0;
                column = cur_size - (diag + 3) / 2;
            } else {
                row = (diag + 1) / 2;
                column = cur_size - 1;
            }
            
            if (way > 0) {
                row += diag_size - 1;
                column -= diag_size - 1;
            }
            for (int i = 0; i < diag_size; ++i) {
                printf("%d ", mas[cur_size - 1 - (row + i * -way)][column - i * -way]);
            }
            
            way *= -1;
        }
        printf("\n");
    }
    
    return 0;
}
