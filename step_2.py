import nltk
import numpy as np 
from nltk import word_tokenize
import string

raw = open('yoda.txt').read()
text = raw.lower()
print(len(text))
# text is 6005 tokens long.


# number of unique words with punctuation:
vocab_punc = sorted(set(word_tokenize(text)))
print(len(vocab_punc))
print(vocab_punc)
words = [w.lower() for w in vocab_punc]
print(words)
