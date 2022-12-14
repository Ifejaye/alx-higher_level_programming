#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_key = {"I": 1, "V": 5, "X": 10, "L":50, "C": 100, "D": 500, "M": 1000}
    answer = 0
    for i in range(len(roman_key)):
        if i > 0 and roman_key[roman_string[i]] < roman_key[roman_string[i + 1]]:
            answer -= roman_key[roman_string[i]]
        else:
            answer += roman_key[roman_string[i]]
    return answer