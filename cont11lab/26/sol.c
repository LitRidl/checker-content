#include <stdio.h>
#include <stdlib.h>

typedef enum {NUMBER, SPACE, OTHER} State;

int is_alp(char c)
{
    return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
}

int is_number(char c)
{
    return (c >= '0') && (c <= '9');
}

int is_sign(char c)
{
    return (c == '+') || (c == '-');
}

int main(void)
{
    State s = SPACE;
    int c = 0, i = 0;
    long long sum = 0, sum1 = 0, sum_old = 0;
    do {
        c = getchar();
        switch (s) {
            case NUMBER:
                if (is_number(c)) {
                    sum1 += c - '0';
                } else if (is_alp(c) || is_sign(c)) {
                    s = OTHER;
                    sum1 = 0;
                } else if (c == ' ' || c == '\t') {
                    i++;
                    s = SPACE;
                    sum_old = sum;
                    sum = sum1;
                } else if (c == '\n' || c == EOF) {
                    sum_old = sum;
                    sum = sum1;
                    i++;
                    if (i > 1) {
                        printf("%lli\n", sum_old);
                    }
                    sum_old = 0;
                    i = 0;
                    s = SPACE;
                }
                break;
            case SPACE:
                if (is_number(c)) {
                    sum1 = c - '0';
                    s = NUMBER;
                } else if (is_sign(c)) {
                    s = NUMBER;
                    sum1 = 0;
                } else if (c == '\n' || c == EOF || c == '\r') {
                } else {
                    s = OTHER;
                }
                break;
            case OTHER:
                if (c == ' ' || c == '\t') {
                    s = SPACE;
                } else if (c == '\n' || c == EOF) {
                    s = SPACE;
                    if (i > 1) {
                        printf("%lli\n", sum_old);
                    }
                    i = 0;
                }
                break;
        }
    } while (c != EOF);
    return 0;
}