/*
13 12 11 10
14  7  8  9
15  6  3  2
16  5  4  1
*/
#include <stdio.h>

int main(void)
{
    int tests, max_size, cur_size, sign;
    scanf("%d%d", &tests, &max_size);
    
    int row, column;
    
    int mas[max_size][max_size];
    int way[2] = {0, 1};
    
    for (int test = 0; test < tests; ++test) {
        scanf("%d", &cur_size);
        for (int i = 0; i < cur_size; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                scanf("%d", &(mas[i][j]));
            }
        }
        
        row = 0;
        column = -1;
        
        for (int i = 0, idx = 0; i < cur_size; ++i) {
            for (int j = 0; j < 2 * i + 1; ++j) {
                if (j == 0 || j == 1 || j == i + 1) {
                    ++idx;
                }
                
                sign = j > i ? -1 : 1;
                
                column += way[idx % 2] * sign;
                row += way[(idx + 1) % 2] * sign;
                // printf("%d %d\n", way[idx % 2] * sign, way[(idx + 1) % 2] * sign);
                
                printf("%d ", mas[cur_size - row - 1][cur_size - column - 1]);
            }
            // printf("\n");
            
        }
        printf("\n");
    }
    return 0;
}

