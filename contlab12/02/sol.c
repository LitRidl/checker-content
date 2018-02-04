#include <stdio.h>
#include <stdlib.h>

int max(int x, int y)
{
    return (x > y) ? x : y;
}

int rec_sum(int number, int max_sum, int max_a)
{
    if (number / 100) {
        return rec_sum(number / 10, abs(number % 10 + number / 10 % 10 + number / 100 % 10), max(max_a, abs(number % 10 + number / 10 % 10 + number / 100 % 10)));
    } else {
        return max_a;
    }
}

int print_numbers(int number)
{
    int number_old = 0, max_sum = 0;
    number_old = number;
    int max_a = rec_sum(number, 0, 0);
    if (number_old / 100) {
        while (number_old / 100) {
            max_sum = abs(number_old % 10 + number_old / 10 % 10 + number_old / 100 % 10);
            if (max_sum == max_a) {
                printf("%03d ", abs(number_old % 1000));
            }
            number_old /= 10;
        }
        printf("\n");
        return 0;
    } else {
        printf("\n");
        return 0;
    }
}

int main(void)
{
    int number = 0;
    while (scanf("%d", &number) == 1) {
        print_numbers(number);
    }
    return 0;
}