/*
есть ли гласная, входящая в состав всех слов
agere sequitur esse
argumenta ponderantur non numerantur
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


Set get_consonants()
{
    Set s = EMPTY_SET;
    for (int c = 'a'; c <= 'z'; ++c) {
        if (is_consonant(c)) {
            s = set_insert(s, get_index(c));
        }
    }
    return s;
}

Set get_vowels()
{
    Set s = EMPTY_SET;
    for (int c = 'a'; c <= 'z'; ++c) {
        if (is_vowel(c)) {
            s = set_insert(s, get_index(c));
        }
    }
    return s;
}


int main(void)
{
    bool result = true;
    
    Set letters_all = set_complement(EMPTY_SET);
    Set letters_word = EMPTY_SET;
    int c = 0;
    while ((c = getchar()) != EOF) {
        if (isspace(c) || iscntrl(c)) {
            if (letters_word) {
                letters_all = set_intersection(letters_all, letters_word);
            }
            letters_word = EMPTY_SET;
            if (set_intersection(get_vowels(), letters_all) == EMPTY_SET) {
                result = false;
                break;
            }
        } else {
            letters_word = set_insert(letters_word, get_index(c));
        }
    }
    if (letters_word != EMPTY_SET) {
        letters_all = set_intersection(letters_all, letters_word);
        if (set_intersection(get_vowels(), letters_all) == EMPTY_SET) {
            result = false;
        }
    }
    
    printf((result && set_complement(letters_all) != EMPTY_SET) ? "Yes\n" : "No\n");
    
    return 0;
}
