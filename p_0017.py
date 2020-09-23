"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

Answer: 21124
"""
import string


def split_number(n):
    pos_nums = []
    while n > 0:
        pos_nums.append(n % 10)
        n = n // 10
    i = 1
    for index, _ in enumerate(pos_nums):
        pos_nums[index] = pos_nums[index] * i
        i *= 10
    return pos_nums[::-1]


def num_to_words(n: int) -> str:
    """
    Only works for numbers from 1 to 1000
    """

    letter_map = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    if n == 0:
        return ""

    if n in letter_map:
        return letter_map[n]

    split_num = split_number(n)

    if n < 100:
        return num_to_words(split_num[-2]) + "-" + letter_map[split_num[-1]]

    if n < 1000:
        word_1 = f"{num_to_words(split_num[-3] // 100)} hundred"
        word_2 = f"{num_to_words(sum(split_num[-2:]))}"
        if word_2:
            word_1 = word_1 + " and " + word_2

        return word_1

    return "one thousand"


def num_letter_count(n: int):
    word = "".join([c for c in num_to_words(n) if c in string.ascii_lowercase])
    return len(word)


def main():
    max_num = 1000
    print(sum(num_letter_count(i) for i in range(1, max_num + 1)))


main()
