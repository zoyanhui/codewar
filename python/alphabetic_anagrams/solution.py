import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.insert(0,parentdir) 
from testtool.testtool import test


import math

def listPosition(word):
  """Return the anagram list position of the word"""
  alphabet_list = sorted(list(w for w in word))
  alphabet_dict = build_alphabet_dict(word)
  position = 1
  for w in word:
    idx = alphabet_list.index(w)  
    first_alphabet_set = set(alphabet_list[:idx])
    for first_w in first_alphabet_set:
        remove_a_alphabet(first_w, alphabet_dict)
        position += factorial_word_dict(alphabet_dict)
        count = alphabet_dict.get(first_w, 0)
        alphabet_dict[first_w] = count + 1    
    del alphabet_list[idx]
    remove_a_alphabet(w, alphabet_dict)
  return position

def build_alphabet_dict(word):
    alphabet_dict = {}
    for w in word:
        count = alphabet_dict.get(w, 0)
        alphabet_dict[w] = count + 1
    return alphabet_dict

def remove_a_alphabet(w, alphabet_dict):
    if alphabet_dict.get(w, None):
        alphabet_dict[w] -= 1
        if alphabet_dict[w] == 0:
            del alphabet_dict[w]

def factorial_word_dict(alphabet_dict):
    dup_total = 1
    total_alphabet = 0
    for k,v in alphabet_dict.items():
        dup_total *= math.factorial(v)
        total_alphabet += v
    return math.factorial(total_alphabet) / dup_total

if __name__ == '__main__':
    testValues = {'A' : 1, 'ABAB' : 2, 'AAAB' : 1, 'BAAA' : 4, 'QUESTION' : 24572, 'BOOKKEEPER' : 10743}
    for word in testValues:
        test.assert_equals(listPosition(word), testValues[word])
    test.run_test()