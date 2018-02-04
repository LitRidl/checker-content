#include <stdio.h>

typedef enum { word1, word2, word3, go_further } State;
typedef int Symbol;

State state = word1;
Symbol symbol;

int main(void)
{
    int number_of_words = 0;
    
    while ((symbol = getchar()) != EOF) {
        switch (state) {
            case word1:
                if ((symbol != ' ') && (symbol != '\n') && (symbol != '\t')) {
                    state = word2;
                }
                break;
 
            case word2:
                if ((symbol != ' ') && (symbol != '\n') && (symbol != '\t')) {
                    state = word3;
                } else {
                    state = word1;
                }
                break;
            
            case word3:
                if ((symbol != ' ') && (symbol != '\n') && (symbol != '\t')) {
                    state = go_further;
                    number_of_words++;
                } else {
                    state = word1;
                }
                break;
                
            case go_further:
                if ((symbol != ' ') && (symbol != '\n') && (symbol != '\t')) {
                    state = go_further;
                } else {
                    state = word1;
                }
                break;
        }
    }

    printf("%d\n", number_of_words);
    return 0;
}
