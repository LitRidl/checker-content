#include <stdio.h>

typedef enum {
    SPACE,
    DIGIT,
    OTHER
} State;

int is_digit(int c)
{
    if ((c >= '0' && c <= '9') || (c >= 'a' && c <= 'f') || (c >= 'A' && c <= 'F')) {
        return 1;
    }
    return 0;
}

int get_value(int c)
{
    int value = 0;
    if (c >= '0' && c <= '9') {
        value = c - '0';
    } else if (c >= 'a' && c <= 'f') {
        value = c - 'a' + 10;
    } else if (c >= 'A' && c <= 'F') {
        value = c - 'A' + 10;
    } if (value % 2) {
        return value;
    }
    return 0;
}

int is_space(int c)
{
    return (c == ' ') || (c == '\t') || (c == '\n') || (c == '\r') || (c == EOF);
}

int main(void)
{
    State s = SPACE;
    int c, sum = 0;
    do {
        c = getchar();
        switch (s) {
            case DIGIT:
                if (is_digit(c)) {
                    sum += get_value(c);
                } else if (is_space(c)) {
                    printf("%X", sum);
                    if (c != EOF) {
                        printf("%c", c);
                    }
                    sum = 0;
                    s = SPACE;
                } else {
                    sum = 0;
                    s = OTHER;
                }
                break;
            case SPACE:
                if (is_digit(c)) {
                    sum += get_value(c);
                    s = DIGIT;
                } else if (!is_space(c)) {
                    s = OTHER;
                } else {
                    if (c != EOF) {
                        printf("%c", c);
                    }
                }
                break;
            case OTHER:
                if (is_space(c)) {
                    s = SPACE;
                    if (c != EOF) {
                        printf("%c", c);
                    }
                }
                break;
        }
    } while (c != EOF);
    printf("\n");
    return 0;
}