import pandas as pd
import numpy as np
import nltk

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')


targets = train.target

tweets = train.text

A = [nltk.word_tokenize(x) for x in tweets]
