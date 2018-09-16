# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 20:43:53 2018

@author: noelg
"""

def check_word_in_tweet(word, data):
    contains_column = data['text'].str.contains(word, case = False)
    contains_column |= data['user-screen_name'].str.contains(word, case = False)
    contains_column |= data['extended_tweet-full_text'].str.contains(word, case = False)
    contains_column |= data['retweeted_status-user-screen_name'].str.contains(word, case = False)
    contains_column |= data['retweeted_status-text'].str.contains(word, case=False)
    contains_column |= data['quoted-status_text'].str.contains(word, case=False)
    return contains_column