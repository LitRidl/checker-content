/*
4  5  6  7
3 14 15  8
2 13 16  9
1 12 11 10
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
        
        row = -1;
        column = 0;
        
        for (int cnt_elems = cur_size, idx = 0; cnt_elems > 0; ++idx, cnt_elems -= idx % 2) {
            for (int i = 0; i < cnt_elems; ++i) {
                column += way[(idx + 3) % 4];
                row += way[idx % 4];
                printf("%d ", mas[cur_size - 1 - row][column]);
            }
        }
        printf("\n");
    }
    
    return 0;
}

