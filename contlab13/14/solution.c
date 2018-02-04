/*
есть ли согласная, не входящая ни в одно слово?
circulus vitiosus
consonantes sunt in litteris Latinis qwrtypsdfghjklzxcvbnm
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


Set get_vowels()
{
    Set s = EMPTY_SET;
    char vowels[] = {'a', 'e', 'i', 'o', 'u'};
    for (int i = 0; i < sizeof(vowels) / sizeof(vowels[0]); ++i) {
        s = set_insert(s, get_index(vowels[i]));
    }
    return s;
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


int main(void)
{
    bool result = true;
    
    Set consonants_in_words = EMPTY_SET;
    int c = 0;
    while ((c = getchar()) != EOF) {
        if (isspace(c) || iscntrl(c)) {
            if (set_intersection(consonants_in_words, get_consonants()) == get_consonants()) {
                break;
            }
        } else {
            if (is_consonant(c)) {
                consonants_in_words = set_insert(consonants_in_words, get_index(c));
            }
        }
    }
    if (set_intersection(consonants_in_words, get_consonants()) == get_consonants()) {
        result = false;
    }
    
    printf(result ? "Yes\n" : "No\n");
    
    return 0;
}