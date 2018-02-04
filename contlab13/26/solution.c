/*
есть ли слово, все согласные которого эксплозивные {t, d, k, g, p, b}
sic itur ad astra
aequilibrium indifferentiae
*/
#include <stdio.h>
#include <ctype.h>

#include <inttypes.h>
#include <stdbool.h>

typedef uint32_t Set;
#define EMPTY_SET ((Set) 0UL)

Set set_insert(Set s, unsigned idx)
{
    return s | ((Set) 1UL << idx);
}

bool set_contains(Set s, unsigned idx)
{
    return s & ((Set) 1UL << idx);
}

Set set_intersection(Set s1, Set s2)
{
    return s1 & s2;
}

Set set_union(Set s1, Set s2)
{
    return s1 | s2;
}

Set set_complement(Set s)
{
    return ~s;
}

Set set_difference(Set s1, Set s2)
{
    return s1 & ~s2;
}

Set set_symmetric_difference(Set s1, Set s2)
{
    return s1 ^ s2;
}


bool is_latin(int c)
{
    c = tolower(c);
    return c >= 'a' && c <= 'z';
}

bool is_vowel(int c)
{
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

bool is_consonant(int c)
{
    c = tolower(c);
    return is_latin(c) && !is_vowel(c);
}


int get_index(int c)
{
    if (islower(c)) {
        return c - 'a';
    }
    return c - 'A';
}

bool is_voice(int c)
{
    c = tolower(c);
    return c == 'b' || c == 'v' || c == 'g' ||
           c == 'd' || c == 'z';
}

bool is_voicelessness(int c)
{
    c = tolower(c);
    return c == 'p' || c == 't' || c == 'k' ||
           c == 'f' || c == 's' || c == 'c' ||
           c == 'q';
}

bool is_sonorant(int c)
{
    c = tolower(c);
    return c == 'm' || c == 'n' || c == 'l' ||
           c == 'h' || c == 'j' || c == 'r' ||
           c == 'w';
}


bool is_plosive(int c)
{
    c = tolower(c);
    return c == 't' || c == 'd' || c == 'k' ||
           c == 'g' || c == 'p' || c == 'b';
}

int main(void)
{
    bool result = false;
    bool word_only_plosive = true, cons = false;
    
    Set letters = EMPTY_SET;
    int c = 0;
    while ((c = getchar()) != EOF) {
        if (isspace(c) || iscntrl(c)) {
            letters = EMPTY_SET;
            if (word_only_plosive && cons) {
                result = true;
                break;
            }
            word_only_plosive = true;
            cons = false;
        } else if (is_consonant(c) && !is_plosive(c)) {
            word_only_plosive = false;
        } else {
            if (is_consonant(c))
                cons = true;
            letters = set_insert(letters, get_index(c));
        }
    }
    if (letters != EMPTY_SET && word_only_plosive && cons) {
        result = true;
    }
    
    printf(result ? "Yes\n" : "No\n");
    
    return 0;
}

