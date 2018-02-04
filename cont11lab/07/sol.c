#include <stdio.h>


typedef enum {SPACE, IN_WORD} State;

State state = SPACE;


int is_lower(char c)
{
    return (c >= 'a' && c <= 'z');
}

int is_upper(char c)
{
    return (c >= 'A' && c <= 'Z');
}

int is_digit(char c)
{
    return (c >= '0' && c <= '9');
}

int other(char c)
{
    return !((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9') || (c == ' ') || (c == '\n') || (c == '\t'));
}


int main(void)
{
    int symbol;
    int key = 3;
    while ((symbol = getchar()) != EOF) {
        switch (state) {
            case SPACE:
                if (is_lower(symbol)) {
                    symbol = ((symbol - 'a' + key) % 26) + 'a';
                    key++;
                    putchar(symbol);
                    state = IN_WORD;
                } else if (is_upper(symbol)) {
                    symbol = ((symbol - 'A' + key) % 26) + 'A';
                    key++;
                    putchar(symbol);
                    state = IN_WORD;
                } else if (is_digit(symbol)) {
                    symbol = ((symbol - '0' + key) % 10) + '0';
                    key++;
                    putchar(symbol);
                    state = IN_WORD;
                } else if (other(symbol)) {
                    key++;
                    putchar(symbol);
                    state = IN_WORD;
                }
                break;
            case IN_WORD:
                if (other(symbol)) {
                    key++;
                    putchar(symbol);
                    state = IN_WORD;
                } else if (is_lower(symbol)) {
                    symbol = ((symbol - 'a' + key) % 26) + 'a';
                    key++;
                    putchar(symbol);
                    state = IN_WORD;
                } else if (is_upper(symbol)) {
                    symbol = ((symbol - 'A' + key) % 26) + 'A';
                    key++;
                    putchar(symbol);
                    state = IN_WORD;
                } else if (is_digit(symbol)) {
                    symbol = ((symbol - '0' + key) % 10) + '0';
                    key++;
                    putchar(symbol);
                    state = IN_WORD;
                } else if (symbol == '\n') {
                    key = 3;
                    putchar('\n');
                    state = SPACE;
                } else if (symbol == ' ') {
                    key = 3;
                    putchar(' ');
                    state = SPACE;
                } else if (symbol == '\t') {
                    key = 3;
                    putchar('\t');
                    state = SPACE;
                }
                break;
        }
    }
    putchar('\n');
    return 0;
}
