#include <stdio.h>

typedef enum {SPACE, DIGIT, OTHER} State;

int is_octal_digit(int c)
{
    return (c >= '0' && c <= '7');
}

int is_space(int c)
{
    return (c == ' ') || (c == '\t') || (c == '\n') || (c == '\r') || (c == EOF);
}

int binary_translation(long long buffer, long long capacity)
{
    capacity /= 10;
    while (capacity != 0) {
        int c = buffer / capacity;
        switch (c) {
            case 0:
                printf("000");
                break;
            case 1:
                printf("001");
                break;
            case 2:
                printf("010");
                break;
            case 3:
                printf("011");
                break;
            case 4:
                printf("100");
                break;
            case 5:
                printf("101");
                break;
            case 6:
                printf("110");
                break;
            case 7:
                printf("111");
                break;
        }
        buffer %= capacity;
        capacity /= 10;
    }
    return 0;
}


int main(void)
{
    State state = SPACE;
    long long buffer = 0, capacity = 1;
    int c = 0;
    do {
        c = getchar();
        switch (state) {
            case DIGIT:
                if (is_octal_digit(c)) {
                    buffer = buffer * 10 + (c - '0');
                    capacity *= 10;
                } else if (is_space(c)) {
                    binary_translation(buffer, capacity);
                    buffer = 0;
                    capacity = 1;
                    if (c != EOF) {
                        printf("%c", c);
                    }
                    state = SPACE;
                } else {
                    state = OTHER;
                    buffer = 0;
                    capacity = 1;
                }
                break;

            case SPACE:
                if (is_octal_digit(c)) {
                    buffer = buffer * 10 + (c - '0');
                    capacity *= 10;
                    state = DIGIT;
                } else if (!is_space(c)) {
                    state = OTHER;
                } else {
                    if (c != EOF) {
                        printf("%c", c);
                    }
                }
                break;

            case OTHER:
                if (is_space(c)) {
                    state = SPACE;
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
