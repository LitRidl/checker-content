#include <stdio.h>

int main(void)
{
    int num;
    while (scanf("%d", &num) == 1) {
        int i = 1;
        int res = num / 10;
        num /= 10;
        while (num / 10 != 0) {
            num /= 10;
            i *= 10;
        }
        res = res - i * num;
        printf("%d\n", res);
    }
    return 0;
}
