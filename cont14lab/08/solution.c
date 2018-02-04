/*
  1  2  6  7
  3  5  8 13
  4  9 12 14
 10 11 15 16
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
        
        way = 1;
        
        for (int diag = 0; diag + 1 < 2 * cur_size; ++diag) {
            diag_size = min(diag + 1, 2 * cur_size - diag - 1);
            row = cur_size - 1 - max(cur_size - diag - 1, 0);
            column = max(diag + 1 - cur_size, 0);
            if (way < 0) {
                row -= diag_size - 1;
                column += diag_size - 1;
            }
            for (int i = 0; i < diag_size; ++i) {
                printf("%d ", mas[row - i * way][column + i * way]);
            }
            way *= -1;
        }
        printf("\n");
    }
    
    return 0;
}


