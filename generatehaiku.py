#!/usr/bin/env python3
# generatehaiku.py

from random import randint

# 2-syllable adjectives
adj2 = ['devo', 'failed', 'passed', 'beta', 'gamma', 'onebox', 'frugal', 'obsessed', 'on call']
7
# 1-syllable nouns
nouns1 = ['slop', 'squid', 'queue', 'chime', 'prod', 'jeff', 'sprint', 'host', 'graph', 'herd', 'roadmap', 'spy', 'sim', 'sage', 'debt']

# 2-syllable nouns
nouns2 = ['draco', 'woola', 'day one', 'the spheres', 'java', 'bias', 'tickets', 'instance', 'python', 'ruby', 'blocker', 'data', 'callout', 'server', 'brazil', 'seller', 'meeting', 'wiki', 'payments', 'demo', 'merlin', 'rollback', 'octane', 'lambda', 'sev two', 'pipeline', 'blind spy', 'reserves', 'mentor', 'cosmos', 'druid', 'game lunch', 'paris']

# 3-syllable nouns
nouns3 = ['amazon', 'resistance', 'deep cover', 'commander','prevention', 'debt control', 'ownership', 'bar raiser', 'bodyguard', 'design doc', 'engineer', 'persistence', 'customer', 'transactions', 'quarantine', 'manager', 'dynamo', 'database', 'production', 'adapter', 'apollo', 'container', 'terminal', 'code review']

# 4-syllable nouns
nouns4 = ['dcs prime', 'disincentives', 'amelia', 'false commander', 'fiona', 'integration', 'frugality', 'auto scaling', 'scaling planner', 'happy hour', 'fact of the day', 'version conflict', 'design review', 'architecture', 'recoveries']

# 1-syllable verbs
verbs1 = ['was', 'took', 'ate', 'made','shoot', 'killed', 'shook', 'fail', 'pass', 'groomed', 'scoped']

# 2-syllable verbs
verbs2 = ['think big', 'earn trust', 'dive deep', 'invent', 'commit', 'git push', 'approve', 'reject', 'succeed', 'fail']

# 3-syllable verbs
verbs3 = ['work from home', 'could be good', 'rotated', 'listened to', 'disagree', 'brazil build', 'unit test', 'have backbone']

def get_haiku() -> str:
    return \
        make_haiku(adj2, nouns3, nouns3, verbs2, adj2, nouns1, nouns4)

def make_haiku(list1, list2, list3, list4, list5, list6, list7) -> str:
    haiku = \
        get_word(list1) + ' ' + get_word(list2) + ' \n' + get_word(list3) + ' ' + get_word(list4) + ' ' + get_word(list5) + ' \n' + get_word(list6) + ' ' + get_word(list7)

    print(haiku)
    return haiku

def get_word(wordlist: str) -> str:
    return wordlist[randint(0, len(wordlist)-1)]

get_haiku()