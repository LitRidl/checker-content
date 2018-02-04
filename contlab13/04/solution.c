/*
есть ли слово, хотя бы одна согласная которого повторяется
crescent
victoriam venit ad fortem
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


int main(void)
{
    bool result = false;
    bool word_consonants_unique = true;
    
    Set letters = EMPTY_SET;
    int c = 0;
    while ((c = getchar()) != EOF) {
        if (isspace(c) || iscntrl(c)) {
            letters = EMPTY_SET;
            if (!word_consonants_unique) {
                result = true;
                break;
            }
            word_consonants_unique = true;
        } else if (is_consonant(c) && set_contains(letters, get_index(c))) {
            word_consonants_unique = false;
        } else {
            letters = set_insert(letters, get_index(c));
        }
    }
    if (letters != EMPTY_SET && !word_consonants_unique) {
        result = true;
    }
    
    printf(result ? "Yes\n" : "No\n");
    
    return 0;
}
