/*
 7  4  2  1
11  8  5  3
14 12  9  6
16 15 13 10
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
    int tests, max_size, cur_size, diag_size;
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
            diag_size = min(diag + 1, 2 * cur_size - diag - 1);
            column = max(cur_size - diag - 1, 0);
            row = max(diag + 1 - cur_size, 0);
            for (int i = 0; i < diag_size; ++i) {
                printf("%d ", mas[row + i][column + i]);
            }
        }
        printf("\n");
    }
    
    return 0;
}

