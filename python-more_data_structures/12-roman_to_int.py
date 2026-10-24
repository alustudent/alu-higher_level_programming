#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i, ch in enumerate(roman_string):
        value = values.get(ch, 0)
        nxt = roman_string[i + 1] if i + 1 < len(roman_string) else None
        if nxt and values.get(nxt, 0) > value:
            total -= value
        else:
            total += value
    return total
