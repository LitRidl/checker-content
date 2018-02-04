/*
 7  6  5 16
 8  1  4 15
 9  2  3 14
10 11 12 13
*/
#include <stdio.h>

int main(void)
{
    int tests, max_size, cur_size;
    scanf("%d%d", &tests, &max_size);
    
    int row, column;
    
    int mas[max_size][max_size];
    
    int way[4] = {1, 0, -1, 0};
    
    for (int test = 0; test < tests; ++test) {
        scanf("%d", &cur_size);
        for (int i = 0; i < cur_size; ++i) {
            for (int j = 0; j < cur_size; ++j) {
                scanf("%d", &(mas[i][j]));
            }
        }
        
        row = 0 + (cur_size - 1) / 2;
        column = 0 + (cur_size - 1) / 2;
        
        for (int cnt_elems = 1, idx = 0;
                row >= 0 && column >= 0 && row < cur_size && column < cur_size;
                ++idx, cnt_elems += (idx + 1) % 2) {
            for (int i = 0; i < cnt_elems; ++i) {
                printf("%d ", mas[row][column]);
                column += way[(idx + 3) % 4];
                row += way[idx % 4];
            }
        }
        printf("\n");
    }
    
    return 0;
}
