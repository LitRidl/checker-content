/*
есть ли слова, начинающиеся и заканчивающиеся гласными
amaretto
affectus sunt non levia
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
    bool word_starts_vowel = false;
    bool word_ends_vowel = false;
    
    int c = 0, prev_word_c = 0;
    int char_counter = 0;
    while ((c = getchar()) != EOF) {
        if (isspace(c) || iscntrl(c)) {
            if (char_counter > 0 && word_starts_vowel && is_vowel(prev_word_c)) {
                result = true;
                break;
            }
            char_counter = 0;
            word_starts_vowel = false;
            word_ends_vowel = false;
        } else {
            ++char_counter;
            if (char_counter == 1 && is_vowel(c)) {
                word_starts_vowel = true;
            }
            prev_word_c = c;
        }
    }
    if (char_counter > 0 && word_starts_vowel && is_vowel(prev_word_c)) {
        result = true;
    }
    
    printf(result ? "Yes\n" : "No\n");
    
    return 0;
}
