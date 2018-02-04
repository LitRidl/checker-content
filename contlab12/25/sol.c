#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int compute(int x)
{
    int y = 0;
    int z = 1;
    int j = 0;
    do {
        y = x % 10;
        if (y % 2 == 0) {
            if (y == 0) {
                if ((x / 10) >= 0) {
                    j = j + 9 * z;
                    y = 1;
                } else if ((x / 10) < 0) {
                    j -= 9 * z;
                    y = -1;
                }
            }
            j += y > 0 ? (y - 1) * z : (y + 1) * z;
        } else {
            j += y * z;
        }
        z = z * 10;
        x /= 10;
    } while (x != 0);
    z = 1;
    return j;
    j = 0;
}


int main(void)
{
    int number = 0;
    while (scanf("%d", &number) == 1) {
        printf("%d\n", compute(number));
    }
    return 0;
}