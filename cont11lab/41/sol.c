#include <stdio.h>
#include <ctype.h>

typedef enum {
    SKIP_DELIMITERS_UNTIL_WORD,
    SUM_DIGITS_UNTIL_NUMBER_END,
    SKIP_UNTIL_WORD_END, SKIP_DELIMITERS,
    SUM_DIGITS_UNTIL_LINE_END,
    SKIP_UNTIL_LINE_END,
    SKIP_ALL_UNTIL_NUMBER
} State;

int main(void)
{
    State s = SKIP_DELIMITERS_UNTIL_WORD;
    int c;
    long long sum = 0, all_sum = 0;
    do {
        c = getchar();
        switch (s) {
            case SKIP_DELIMITERS_UNTIL_WORD:
                if (c == ' ' || c == '\t' || c == '\n' || c == '\r') {
                    s = SKIP_DELIMITERS_UNTIL_WORD;
                } else if (isdigit(c)) {
                    if (((c - '0') % 2) == 0) {
                        sum += c - '0';
                    }
                    s = SUM_DIGITS_UNTIL_NUMBER_END;
                } else {
                    s = SKIP_UNTIL_WORD_END;
                }
                break;
 
            case SUM_DIGITS_UNTIL_NUMBER_END:
                if (c == ' ' || c == '\t') {
                    all_sum += sum;
                    sum = 0;
                    printf("%lld", all_sum);
                    all_sum = 0;
                    s = SKIP_DELIMITERS;
                } else if (isdigit(c)) {
                    if (((c - '0') % 2) == 0) {
                        sum += c - '0';
                    }
                    s = SUM_DIGITS_UNTIL_NUMBER_END;
                } else if (c == '\n' || c == '\r' || c == EOF) {
                    all_sum += sum;
                    sum = 0;
                    printf("%lld", all_sum);
                    printf("\n");
                    all_sum = 0;
                    s = SKIP_DELIMITERS_UNTIL_WORD;
                } else {
                    sum = 0;
                    s = SKIP_UNTIL_WORD_END;
                }
                break;
 
            case SKIP_UNTIL_WORD_END:
                if (c == ' ' || c == '\t') {
                    s = SKIP_ALL_UNTIL_NUMBER;
                } else if (c == '\n' || c == '\r') {
                    s = SKIP_DELIMITERS_UNTIL_WORD;
                } else {
                    s = SKIP_UNTIL_WORD_END;
                }
                break;
 
            case SKIP_DELIMITERS:
                if (c == ' ' || c == '\t') {
                    s = SKIP_DELIMITERS;
                } else if (c == '\n' || c == '\r' || c == EOF) {
                    s = SKIP_DELIMITERS_UNTIL_WORD;
                    printf("\n");
                } else if (isdigit(c)) {
                    if (((c - '0') % 2) == 0) {
                        sum += c - '0';
                    }
                    s = SUM_DIGITS_UNTIL_LINE_END;
                } else {
                    s = SKIP_UNTIL_LINE_END;
                }
                break;
 
            case SUM_DIGITS_UNTIL_LINE_END:
                if (c == ' ' || c == '\t') {
                    all_sum += sum;
                    sum = 0;
                    printf(" %lld", all_sum);
                    all_sum = 0;
                    s = SKIP_DELIMITERS;
                } else if (c == '\n' || c == '\r' || c == EOF) {
                    all_sum += sum;
                    sum = 0;
                    printf(" %lld", all_sum);
                    printf("\n");
                    all_sum = 0;
                    s = SKIP_DELIMITERS_UNTIL_WORD;
 
                } else if (isdigit(c)) {
                    if (((c - '0') % 2) == 0) {
                        sum += c - '0';
                    }
                    s = SUM_DIGITS_UNTIL_LINE_END;
                } else {
                    sum = 0;
                    s = SKIP_UNTIL_LINE_END;
                }
                break;
 
            case SKIP_UNTIL_LINE_END:
                if (c == ' ' || c == '\t') {
                    s = SKIP_DELIMITERS;
                } else if (c == '\n' || c == '\r' || c == EOF) {
                    printf("\n");
                    s = SKIP_DELIMITERS_UNTIL_WORD;
                } else {
                    s = SKIP_UNTIL_LINE_END;
                }
                break;

            case SKIP_ALL_UNTIL_NUMBER:
                if (c == ' ' || c == '\t') {
                    s = SKIP_ALL_UNTIL_NUMBER;
                } else if (c == '\n' || c == '\r') {
                    s = SKIP_DELIMITERS_UNTIL_WORD;
                } else if (isdigit(c)) {
                    if (((c - '0') % 2) == 0) {
                        sum += c - '0';
                    }
                    s = SUM_DIGITS_UNTIL_NUMBER_END;
                } else {
                    s = SKIP_UNTIL_WORD_END;
                }
                break;
        }
    } while (c != EOF);
    return 0;
}