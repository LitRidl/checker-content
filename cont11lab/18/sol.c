#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

int all(char c)
{
    return !((c >= '0' && c <= '9') || c == ' ' || c == 'C' || c == '\n' || c == '-' || c == '+' || c == '\v');
}

long double c_f(long double c)
{
    return (c * 9) / 5 + 32;
}

int letters(char c)
{
    return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
}

int tabn(char c)
{
    return !(c == ' ' || c == '\n' || c == '\t' || c == '-' || c == '+' || c == '\v');
}

int main(void)
{
    int symbol;
    long double m = 0.0;
    long double s = 0.0;
    int state = 0;
    long double f = 0.0;
    long double r = 0.0;
    long int l = 0;
    long int k = 0;
    int q = 0;

    while ((symbol = getchar()) != EOF) {
        switch (state) {
            case 0:
                if (symbol == ' ' || symbol == '\t') {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    state = 0;
                } else if (symbol == '\n' || symbol == '\v') {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    printf("\n");
                    state = 0;
                } else if (letters(symbol)) {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    state = 1;
                } else if (symbol >= '0' && symbol <= '9') {
                    m = (s * 10) + (symbol - '0');
                    s = m;
                    state = 5;
                } else if (symbol == '-') {
                    state = 6;
                } else if (symbol == '+') {
                    state = 3;
                }
                break;
            case 1:
                if (all(symbol)) {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    state = 1;
                } else if (symbol == ' ' || symbol == '\t') {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    state = 0;
                } else if (symbol == '\n' || symbol == '\v') {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    printf("\n");
                    state = 0;
                }
                break;
            case 2:
                if (symbol == ' ' || symbol == '\t') {
                    printf("%ld%s", l, "F ");
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    state = 0;
                } else if (tabn(symbol)) {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    state = 1;
                } else if (symbol == '\n' || symbol == '\v') {
                    printf("%ld%s\n", l, "F ");
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    state = 0;
                } else if (symbol == '+' || symbol == '-') {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    state = 1;
                }
                break;
            case 3:
                if (symbol == ' ' || symbol == '\t') {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    state = 0;
                } else if (symbol == '\n' || symbol == '\v') {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    printf("\n");
                    state = 0;
                } else if (letters(symbol)) {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    state = 1;
                } else if (symbol >= '0' && symbol <= '9') {
                    m = (s * 10) + (symbol - '0');
                    s = m;
                    state = 5;
                } else if (symbol == '-' || symbol == '+') {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    state = 1;
                }
                break;
            case 4:
                if (symbol >= '0' && symbol <= '9') {
                    m = (s * 10) - (symbol - '0');
                    s = m;
                    state = 4;
                } else if (symbol == 'C') {
                    f = round(c_f(s));
                    l = f;
                    r = l;
                    q = 1;
                    state = 2;
                } else if (all(symbol)) {
                    s = 0;
                    q = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    state = 1;
                } else if (symbol == ' ' || symbol == '\t') {
                    s = 0;
                    m = 0;
                    f = 0;
                    q = 0;
                    r = 0;
                    l = 0;
                    state = 0;
                } else if (symbol == '\n' || symbol == '\v') {
                    s = 0;
                    m = 0;
                    q = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    printf("\n");
                    state = 0;
                } else if (symbol == '-' || symbol == '+') {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    q = 0;
                    l = 0;
                    state = 1;
                }
                break;
            case 5:
                if (symbol >= '0' && symbol <= '9') {
                    m = (s * 10) + (symbol - '0');
                    s = m;
                    state = 5;
                } else if (symbol == 'C') {
                    f = round(c_f(s));
                    l = f;
                    r = l;
                    state = 2;
                } else if (all(symbol)) {
                    s = 0;
                    q = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    state = 1;
                } else if (symbol == ' ' || symbol == '\t') {
                    s = 0;
                    m = 0;
                    f = 0;
                    q = 0;
                    r = 0;
                    l = 0;
                    state = 0;
                } else if (symbol == '\n' || symbol == '\v') {
                    s = 0;
                    m = 0;
                    q = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    printf("\n");
                    state = 0;
                } else if (symbol == '-' || symbol == '+') {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    q = 0;
                    l = 0;
                    state = 1;
                }
                break;
            case 6:
                if (symbol == ' ' || symbol == '\t') {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    state = 0;
                } else if (symbol == '\n' || symbol == '\v') {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    printf("\n");
                    state = 0;
                } else if (letters(symbol)) {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    state = 1;
                } else if (symbol >= '0' && symbol <= '9') {
                    m = (s * 10) - (symbol - '0');
                    s = m;
                    state = 4;
                } else if (symbol == '-' || symbol == '+') {
                    s = 0;
                    m = 0;
                    f = 0;
                    r = 0;
                    l = 0;
                    q = 0;
                    state = 1;
                }
                break;
        }
    }
    if (r != 0) {
        k = floor(round(r));
        r = k;
        printf("%ld%s", k, "F");
    } else if (q == 1) {
        k = floor(round(r));
        r = k;
        printf("%ld%s", k, "F");
    }
    printf("\n");
    return 0;
}