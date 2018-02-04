/*
15 13  7  1
14  6  2 10
 5  3  9 11
 4  8 12 16
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
    
    for (int test = 0; test < tests; ++test) {
        scanf("%d", &cur_size);
        for (int i = 0; i < cur_size; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                scanf("%d", &(mas[i][j]));
            }
        }
        
        
        
        for (int diag = 0; diag + 1 < 2 * cur_size; ++diag) {
            diag_size = cur_size - (diag + 1) / 2;
            
            if (((diag + 1) / 2) % 2 == 0) {
                way = 1;
            } else {
                way = -1;
            }
            
            if ((diag / 2) % 2 == 0) {
                row = 0;
                column = cur_size - (diag + 3) / 2;
            } else {
                row = (diag + 1) / 2;
                column = cur_size - 1;
            }
            
            if (way < 0) {
                row += diag_size - 1;
                column -= diag_size - 1;
            }
            for (int i = 0; i < diag_size; ++i) {
                printf("%d ", mas[row + i * way][column - i * way]);
            }
            
        }
        printf("\n");
    }
    
    return 0;
}


