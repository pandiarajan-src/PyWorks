"""
 Write a Python program to find the longest word in a file.
"""

import re


def find_longest_word_in_a_file(filename: str) -> str:
    with open(filename, 'r') as file:
        file_content = file.read()
        sorted_words = sorted(re.split("[ \n]+", file_content), key=len, reverse=True)
        return sorted_words[0] if len(sorted_words) > 0 else ''
