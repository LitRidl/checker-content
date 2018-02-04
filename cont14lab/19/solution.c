/*
  1  2  9 10
  4  3  8 11
  5  6  7 12
 16 15 14 13
*/
/*
+1 +0

+0 +1

+1 +0
+0 -1

+1 +0

+0 +1
+0 +1
-1 +0
-1 +0

+0 +1

+1 +0
+1 +0
+1 +0
+0 -1
+0 -1
+0 -1
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
        
        row = -1;
        column = 0;
        
        for (int i = 0, idx = 0; i < cur_size; ++i) {
            for (int j = 0; j < 2 * i + 1; ++j) {
                if (j == 0 || j == 1 || j == i + 1) {
                    ++idx;
                }
                
                sign = j > i ? -1 : 1;
                
                row += way[idx % 2] * sign;
                column += way[(idx + 1) % 2] * sign;
                // printf("%d %d\n", way[idx % 2] * sign, way[(idx + 1) % 2] * sign);
                
                printf("%d ", mas[row][column]);
            }
            // printf("\n");
            
        }
        printf("\n");
    }
    return 0;
}
