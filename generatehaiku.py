#!/usr/bin/env python3
# generatehaiku.py

import re
from random import randint
from nltk.corpus import wordnet as wn

# 2-syllable adjectives
adj2 = ['devo', 'failed', 'passed', 'beta', 'gamma', 'onebox', 'frugal', 'obsessed', 'on call', 'ruby', 'data', 'brazil', 'python', 'java', 'hydra', 'docker', 'seller', 'lambda', 'mentor', 'game lunch', 'team lunch', 'server']

# 1-syllable nouns
nouns1 = ['slop', 'squid', 'queue', 'chime', 'prod', 'jeff', 'sprint', 'host', 'graph', 'herd', 'spy', 'sim', 'sage', 'debt']

# 2-syllable nouns
nouns2 = ['draco', 'feature', 'woola', 'day one', 'the spheres', 'bias', 'blocker', 'callout', 'meeting', 'wiki', 'payments', 'demo', 'merlin', 'rollback', 'octane', 'sev two', 'pipeline', 'blind spy', 'reserves', 'cosmos', 'druid', 'paris', 'stand up']

# 3-syllable nouns
nouns3 = ['amazon', 'resistance', 'deep cover', 'commander','prevention', 'debt control', 'ownership', 'bar raiser', 'bodyguard', 'design doc', 'engineer', 'persistence', 'customer', 'transactions', 'quarantine', 'manager', 'dynamo', 'database', 'production', 'adapter', 'apollo', 'container', 'terminal', 'code review']

# 4-syllable nouns
nouns4 = ['dcs prime', 'disincentives', 'amelia', 'false commander', 'fiona', 'integration', 'frugality', 'auto scaling', 'scaling planner', 'happy hour', 'fact of the day', 'version conflict', 'design review', 'architecture', 'recoveries']

# 1-syllable verbs
verbs1 = ['was', 'took', 'ate', 'made','shoot', 'killed', 'shook', 'pass', 'groomed', 'scoped', 'blocked']

# 2-syllable verbs
verbs2 = ['think big', 'earn trust', 'dive deep', 'hire','invent', 'commit', 'git push', 'unblock', 'approve', 'reject', 'succeed']

# 3-syllable verbs
verbs3 = ['work from home', 'interview', 'could be good', 'rotated', 'listened to', 'reinstate', 'downgrade', 'deprecate', 'disagree', 'brazil build', 'unit test', 'have backbone']

def get_haiku() -> str:
    haiku_format = randint(0, 3)
    if haiku_format == 0:
        return make_haiku(nouns2, nouns3, nouns3, verbs2, nouns2, nouns1, nouns4)
    elif haiku_format == 1:
        return make_haiku(nouns2, verbs3, nouns2, verbs1, nouns4, adj2, nouns3)
    elif haiku_format == 2:
        return make_haiku(nouns3, verbs2, nouns4, verbs2, nouns1, nouns3, nouns2)
    else:
        return make_haiku(adj2, nouns3, nouns3, nouns3, nouns1, nouns2, verbs3)

def make_haiku(list1, list2, list3, list4, list5, list6, list7) -> str:
    haiku = \
        get_word(list1) + ' ' + get_word(list2) + ', \n' \
        + get_word(list3) + ' ' + get_word(list4) + ' ' + get_word(list5) + ', \n' \
        + get_word(list6) + ' ' + get_word(list7)
    print(haiku)
    return haiku

def get_word(wordlist: str) -> str:
    return wordlist[randint(0, len(wordlist)-1)]

def add_word(word: str):
    word_type = get_word_type(word)
    num_syllables = get_num_syllables(word)
    if word_type == 'n': # noun
        return None
    elif word_type == 'v': # verb
        return None
    elif word_type == 'a' or word_type == 's': # adjective / adjective satellite
        return None
    elif word_type == 'r': # adverb
        return None

def get_word_type(word: str) -> str:
    return wn.synsets(w)[0].pos()

def get_num_syllables(word: str):
    regex = r"([^aeiouy])(a|e|i|o|u|y)"
    matches = re.findall(regex, word, re.MULTILINE)
    count = len(matches)
    if ['a', 'e', 'i', 'o', 'u'].__contains__(word[0]):
        count += 1
    return count

get_haiku()