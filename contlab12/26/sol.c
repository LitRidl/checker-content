#include <stdio.h>
#include <stdlib.h>

long long int consecutive_numbers_sum(long long int input_number)
{
    int last_symbol = 0;
    int last2_symbol = 0;
    int two_symbols = 0;
    int part_of_a_number = 0;
    int q = 0, m = 0;
    long long int finish_number;
    long long int b = 0, part = 0;
    long long int d, c;
    int n = 0, s = 0;

    if (input_number < 0) {
        q = 1;
        input_number = input_number * (-1);
    }
    while (input_number > 9) {
        last_symbol = input_number % 10;
        last2_symbol = ((input_number % 100) - last_symbol) / 10;
        two_symbols = last_symbol + last2_symbol;
        input_number = input_number / 100;
        if (two_symbols >= 10) {
            part_of_a_number = ((last2_symbol * 10) + last_symbol);
            part = part_of_a_number;
            d = b;
            while (b > 0) {
                b /= 10;
                part *= 10;
            }
            if (n != 0 && part != 0) {
                for (int i = 0; i < n; i++) {
                    part *= 1000;
                }
                n = 0;
            }
            b = d + part;
        } else if (two_symbols < 10) {
            part_of_a_number = ((two_symbols * 100) + (last2_symbol * 10) + last_symbol);
            part = part_of_a_number;
            if (n != 0 && part != 0) {
                for (int i = 0; i < n; i++) {
                    part *= 1000;
                }
                n = 0;
            }
            if (part != 0) {
                d = b;
                while (b > 0) {
                    b /= 10;
                    part *= 10;
                }
                b = d + part;
            } else if (part == 0) {
                n += 1;
            }
        }
    }
    c = b;
    while (b > 0) {
        b /= 10;
        input_number *= 10;
    }
    if (n != 0) {
        for (int i = 0; i < n; i++) {
            input_number *= 1000;
        }
        n = 0;
    }
    b = input_number + c;
    finish_number = b;
    if (q == 1) {
        finish_number = finish_number * (-1);
    }

    return finish_number;
}

int main(void)
{
    int number = 0;
    while (scanf("%d", &number) == 1) {
        printf("%lld\n", consecutive_numbers_sum(number));
    }
    return 0;
}