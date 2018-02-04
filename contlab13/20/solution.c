/*
есть ли слово, содержащее одну согласную, возможно несколько раз
viva ratio
sacrificium intellectus
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

int set_size(Set s)
{
    int count = 0;
    for (; s; s >>= 1) {
        count += s & (Set) 1UL;
    }
    return count;
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
    bool result = false;
    
    Set letters = EMPTY_SET;
    int c = 0;
    while ((c = getchar()) != EOF) {
        if (isspace(c) || iscntrl(c)) {
            if (letters && set_size(set_intersection(letters, get_consonants())) == 1) {
                break;
            }
            letters = EMPTY_SET;
        } else {
            letters = set_insert(letters, get_index(c));
        }
    }
    if (letters != EMPTY_SET && set_size(set_intersection(letters, get_consonants())) == 1) {
        result = true;
    }
    
    printf(result ? "Yes\n" : "No\n");
    
    return 0;
}
