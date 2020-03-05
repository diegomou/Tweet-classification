import pandas as pd
import numpy as np
import nltk

sentence = 'The dog´s house is very ugly!. Because of that, I will sell it.'

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(sentence)

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')


targets = train.target

tweets = train.text

A = [nltk.word_tokenize(x) for x in tweets]