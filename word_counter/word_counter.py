# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import collections
import re

__all__ = [
    'solution',
]

"""
Given a text input, the objective of this Kata is to return the 5 least and
most common words, ordered, with the number of times each of this words appear
in the text.

For example, with this text as input:
'''
This is a text. This text has words that are part of this text.
Each word of this text is a word in the english language
'''

The result should be:
(
    [('are', 1), ('has', 1), ('words', 1), ('part', 1), ('that', 1)],
    [('text', 4), ('this', 4), ('a', 2), ('is', 2), ('word', 2)],
)

Example text: http://pastebin.com/raw/xkTYv7nf
"""


def solution(text):
    word_counter = collections.Counter(re.findall(r'\w+', text.lower()))
    most_common = word_counter.most_common(len(word_counter))

    return (
        sorted(most_common[-5:], key=lambda t: (t[1], t[0])),
        sorted(most_common[:5], key=lambda t: (-t[1], t[0]))
    )
