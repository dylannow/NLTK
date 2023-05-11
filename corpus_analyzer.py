import nltk
from nltk import word_tokenize, sent_tokenize
import pandas as pd

# Initialize corpus
raw = open("yoda.txt").read()
corpus = raw.lower()
corpus = corpus.replace("\n", " ")

# Length of corpus
length_corpus = len(corpus)

# Length of sentences
sentences = sent_tokenize(corpus)
amount_sentences = len(sentences)

# Number of unique words
vocab_punc = sorted(set(word_tokenize(corpus)))
words = [w.lower() for w in vocab_punc]
hapaxes = len(words)

# Average sentence length in characters
total_characters = 0
for i in sentences:
    total_characters += len(i)
average_sentence_length = total_characters / len(sentences)

# Most frequent words
freq_dist = nltk.FreqDist(word_tokenize(corpus))
most_frequent_words = freq_dist.most_common(20)

# Visualize the data
data = {"Most frequent words": most_frequent_words}
df = pd.DataFrame(data)
df.index = pd.RangeIndex(start=1, stop=len(df) + 1)
print(df)
print(f"Length of the text in characters: {length_corpus}")
print(f"Amount of sentences in corpus: {amount_sentences}")
print(f"Number of unique words: {hapaxes}")
print(f"Avarage sentence length: {average_sentence_length}")
