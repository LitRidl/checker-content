#include <stdio.h>
#include <stdlib.h>

typedef enum {SPACE, OTHER} State;

int not_space(int c)
{
    return c != ' ' && c != '\t' && c != '\n' && c != '\r' && c != EOF;
}
int main(void)
{
    State s = SPACE;
    int c = 0, i = 0, copacity = 0;
    do {
        c = getchar();
        switch (s) {
            case SPACE:
                if (not_space(c)) {
                    s = OTHER;
                    i = 1;
                }
                break;
            case OTHER:
                if (not_space(c)) {
                    i += 1;
                } else if (i < 4) {
                    copacity += 1;
                    i = 0;
                    s = SPACE;
                } else {
                    i = 0;
                    s = SPACE;
                }
                break;
        }
    } while (c != EOF);
    printf("%d\n", copacity);
    return 0;
}