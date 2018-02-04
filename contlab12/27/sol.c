#include <stdio.h>


int abs(int x)
{
    return x > 0 ? x : -x;
}

long long change(int number_in)
{
    long long number_out = 0, capacity;
    int sign_value = (number_in < 0) ? -1 : 1;
    long long buffer_number = number_in;
    buffer_number = (buffer_number > 0) ? buffer_number : -buffer_number;
    for (capacity = 1; buffer_number >= 10; capacity *= 1000) {
        int one = buffer_number % 10;
        buffer_number /= 10;
        int ten = buffer_number % 10;
        buffer_number /= 10;
        number_out += (abs(one - ten) * 100 + ten * 10 + one) * capacity;
    }
    return number_out = (number_out + buffer_number * capacity) * sign_value;
}


int main(void)
{
    int number_in = 0;
    while (scanf("%d", &number_in) == 1) {
        printf("%lld\n", change(number_in));
    }
    return 0;
}
