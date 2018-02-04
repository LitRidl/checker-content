#include <stdio.h>


int main(void)
{
    int num_in = 0;
    while (scanf("%d", &num_in) == 1) {
        int capacity = 0;
        num_in = (num_in > 0) ? num_in : -num_in;

        while (num_in > 100) {
            int buf_num = num_in;
            int one = buf_num % 10;
            buf_num /= 10;
            int ten = buf_num % 10;
            buf_num /= 10;
            int hundred = buf_num % 10;
            if (hundred == one + ten) {
                printf("%d ", hundred);
            }
            num_in /= 10;
        }
        printf("\n");
    }
    return 0;
}