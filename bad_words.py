#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 20:21:50 2018

Write a function to detect bad language.

@author: Thomas Bury and Bae
"""

import numpy as np
import pandas as pd

bad_words = pd.read_csv('bad_words.csv', header=None)

# Returns True if text contains bad language.
def contains_badwords(text):
    words = text.split()
    
    for word in words:
        for bad_word in bad_words[0]:
            if bad_word == word:
#                print(bad_word)
#                print(word)
                return True
    return False



