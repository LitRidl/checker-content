/*
есть ли слово, все согласные которого глухие {p, t, k, f, s, c, q}
castis omnia casta
anathemus
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

int main(void)
{
    bool result = false;
    bool word_only_voicelessness = true, cons = false;
    
    Set letters = EMPTY_SET;
    int c = 0;
    while ((c = getchar()) != EOF) {
        if (isspace(c) || iscntrl(c)) {
            letters = EMPTY_SET;
            if (word_only_voicelessness && cons) {
                result = true;
                break;
            }
            word_only_voicelessness = true;
            cons = false;
        } else if (is_consonant(c) && !is_voicelessness(c)) {
            word_only_voicelessness = false;
        } else {
            if (is_consonant(c))
                cons = true;
            letters = set_insert(letters, get_index(c));
        }
    }
    if (letters != EMPTY_SET && word_only_voicelessness && cons) {
        result = true;
    }
    
    printf(result ? "Yes\n" : "No\n");
    
    return 0;
}
