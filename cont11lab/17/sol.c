#include <stdio.h>
#include <ctype.h>

typedef enum {
    DEFINITION_SIGN,
    ACCUM_NUMBER,
    CONFIRMED_OUT,
    WAIT_NEW_WORDS,
    ACCUM_LEAD_ZERO
} State;

int is_ternary(char s)
{
    return (s >= '0' && s <= '2');
}
int output_of_zero(int lead_zero)
{
    while (lead_zero > 0) {
        printf("0");
        --lead_zero;
    }
    return lead_zero;
}
int main(void)
{
    int state = DEFINITION_SIGN;
    long num = 0;
    int sign = 0;
    int zero = '0';
    int lead_zero = 0;
    int s = 0;

    while ((s = getchar()) != EOF) {
        switch (state) {
            case DEFINITION_SIGN:
                num = 0;
                lead_zero = 0;
                sign = 0;
                if (s == '-') {
                    state = ACCUM_LEAD_ZERO;
                    sign = -1;
                } else if (s == '+') {
                    state = ACCUM_LEAD_ZERO;
                    sign = 1;
                } else if (s == '0') {
                    ++lead_zero;
                    state = ACCUM_LEAD_ZERO;
                } else if (is_ternary(s)) {
                    state = ACCUM_NUMBER;
                    num = num * 10 + s - zero;
                } else if (s == '\n') {
                    printf("\n");
                } else if ((s == ' ') || (s == '\t')) {
                    state = DEFINITION_SIGN;
                }  else {
                    state = WAIT_NEW_WORDS;
                }
                break;
            case ACCUM_NUMBER:
                if (s == '0') {
                    state = CONFIRMED_OUT;
                    num = num * 10;
                } else if (is_ternary(s)) {
                    num = num * 10 + s - zero;
                } else if ((s == ' ') || (s == '\t')) {
                    state = DEFINITION_SIGN;
                } else if (s == '\n') {
                    state = DEFINITION_SIGN;
                    printf("\n");
                } else {
                    state = WAIT_NEW_WORDS;
                }
                break;
            case CONFIRMED_OUT:
                if (s == '\n') {
                    if (sign == -1) {
                        printf("-");
                    } else if (sign == 1) {
                        printf("+");
                    }
                    lead_zero = output_of_zero(lead_zero);
                    printf("%ld\n", num);
                    state = DEFINITION_SIGN;
                } else if (s == ' ') {
                    if (sign == -1) {
                        printf("-");
                    } else if (sign == 1) {
                        printf("+");
                    }
                    lead_zero = output_of_zero(lead_zero);
                    printf("%ld ", num);
                    state = DEFINITION_SIGN;
                } else if (s == '0') {
                    state = CONFIRMED_OUT;
                    num = num * 10 + s - zero;
                } else if (s == '\t') {
                    if (sign == -1) {
                        printf("-");
                    }
                    lead_zero = output_of_zero(lead_zero);
                    printf("%ld ", num);
                    state = DEFINITION_SIGN;
                } else if (is_ternary(s)) {
                    state = ACCUM_NUMBER;
                    num = num * 10 + s - zero;
                } else {
                    state = WAIT_NEW_WORDS;
                }
                break;
            case WAIT_NEW_WORDS:
                if ((s == ' ') || (s == '\t')) {
                    state = DEFINITION_SIGN;
                } else if (s == '\n') {
                    state = DEFINITION_SIGN;
                    printf("\n");
                } else {
                    state = WAIT_NEW_WORDS;
                }
                break;
            case ACCUM_LEAD_ZERO:
                if (s == '0') {
                    ++lead_zero;
                    state = ACCUM_LEAD_ZERO;
                } else if (is_ternary(s)) {
                    num = num * 10 + s - zero;
                    state = ACCUM_NUMBER;
                } else if (s == '\n') {
                    if (lead_zero > 0) {
                        if (sign == -1) {
                            printf("-");
                        } else if (sign == 1) {
                            printf("+");
                        }
                        lead_zero = output_of_zero(lead_zero);
                    }
                    printf("\n");
                    state = DEFINITION_SIGN;
                } else if ((s == ' ') || (s == '\t')) {
                    if (lead_zero > 0) {
                        if (sign == -1) {
                            printf("-");
                        } else if (sign == 1) {
                            printf("+");
                        }
                        lead_zero = output_of_zero(lead_zero);
                    }
                    printf(" ");
                    state = DEFINITION_SIGN;
                } else {
                    state = WAIT_NEW_WORDS;
                }
                break;
        }
    }
    if (state == CONFIRMED_OUT) {
        if (sign == -1) {
            printf("-");
        } else if (sign == 1) {
            printf("+");
        }
        lead_zero = output_of_zero(lead_zero);
        printf("%ld", num);
    } else if (state == ACCUM_LEAD_ZERO) {
        if (lead_zero > 0) {
            if (sign == -1) {
                printf("-");
            } else if (sign == 1) {
                printf("+");
            }
            lead_zero = output_of_zero(lead_zero);
        }
    }
    printf("\n");
    return 0;
}


