#include <stdio.h>

int main(void)
{
    int input, f = 0;

    while (scanf("%d", &input) == 1) {
        input = input < 0 ? -input : input;
        
        while (input >= 10) {
            if (input % 10 == input / 10 % 10) {
                f = 1;
                break;
            }
            
            input /= 10;
        }
        f == 1 ? printf("True\n") : printf("False\n");
        f = 0;
    }
    
    return 0;
}
