#include <stdio.h>


long long del(int num_in)
{
    long long num_out = 0, capacity;
    int sign_value = (num_in < 0) ? -1 : 1;
    long long num_in_two = num_in;
    num_in_two = (num_in_two > 0) ? num_in_two : -num_in_two;

    if (num_in_two < 10) {
        return num_in_two * sign_value;
    } else if (num_in_two < 100) {
        return 0;
    } else {
        long long buf_num = num_in_two, buf_num_two = num_in_two;
        for (capacity = 1; buf_num / 10; capacity *= 10) {
            buf_num /= 10;
        }
        num_out = buf_num * (capacity / 10) + buf_num_two % (capacity / 10);
        if (num_out / 100) {
            num_out = (num_out / 100) * 10 + num_out % 10;
        }
    }
    return num_out * sign_value;
}

int main(void)
{
    int num_in = 0;
    while (scanf("%d", &num_in) == 1) {
        printf("%lld\n", del(num_in));
    }
    return 0;
}
