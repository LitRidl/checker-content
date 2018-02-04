#include <stdio.h>

int main(void)
{
    long long sum = 0;
    char symbol;
    int state = 1;

    do {
        symbol = getchar();
        switch (state) {
            case 1:
                if ((symbol != ' ') && (symbol != '\n') && (symbol != '\t'))  {
                    sum += symbol;
                    state = 2;
                }
                break;
            case 2:
                if ((symbol != ' ') && (symbol != '\n') && (symbol != EOF) && (symbol != '\t')) {
                    sum += symbol;
                    state = 2;
                } else {
                    sum = sum % 255;
                    printf("%lld%c", sum, symbol != EOF ? symbol : '\n');
                    sum = 0;
                    state = 1;
                }
                break;
        }
    } while (symbol != EOF);
    return 0;
}
