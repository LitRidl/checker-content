#include <stdio.h>
#define FIRST_DERGEE 10
#define SECOND_DEGREE 100
 
int main(void)
{
    int sign = 1;
    int step = 10;
    int num = 0;
    int rank = 0;
    int piece1 = 0;
    int piece2 = 0;
    int piece3 = 0;
    while (scanf("%d", &num) != EOF) {
        while ((num > SECOND_DEGREE) || (num < -SECOND_DEGREE)) {
            if (num < 0) {
                sign = -1;
            } else {
                sign = 1;
            }
            rank = num;
            piece1 = (rank % (sign * step)) * sign;
            rank = (rank * sign - piece1) / step;
            piece2 = rank % (step);
            rank = (rank - piece2) / (step);
            piece3 = rank % (step);
 
            if ((piece3 < piece2) && (piece2 < piece1)) {
                rank = piece3 * SECOND_DEGREE + piece2 * FIRST_DERGEE + piece1;
                printf("%03d ", rank);
            }
            num = (num - sign * piece1) / (sign * step);
        }
        printf("\n");
    }
    return 0;
}