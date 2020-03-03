import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
import re

import functions_NLP as f_NLP

class data_maniputation:
    def __init__(self):
        self.raw_train = None
        self.raw_test = None
        
        self.raw_tweet_train = None
        self.raw_tweet_test = None
        
        self.target = None
        
        self.tweet_prepro_train = None
        self.tweet_prepro_test = None
    
    def load_data(self):
        self.raw_train = pd.read_csv('train.csv')
        self.raw_test = pd.read_csv('test.csv')
        
        self.target_train = self.raw_train.target
        self.raw_tweet_train = self.target_train.text
        self.raw_tweet_test = self.target_test.text
       
    def prepro_tweets(self):
        self.tweet_prepro_train = [f_NLP.label_url(x) for x in self.raw_tweet_train]
        self.tweet_prepro_test = [f_NLP.label_url(x) for x in self.raw_tweet_test]
        
        self.tweet_prepro_train = [f_NLP.label_hashtag(x) for x in self.tweet_prepro_train]
        self.tweet_prepro_test = [f_NLP.label_hashtag(x) for x in self.tweet_prepro_test]
        
        self.tweet_prepro_train = [f_NLP.label_mention(x) for x in self.tweet_prepro_train]
        self.tweet_prepro_test = [f_NLP.label_mention(x) for x in self.tweet_prepro_test]
        
    def tokenizador(self):      
        self.tweet_tokenized_train = [nltk.word_tokenize(x.lower()) for x in tweet_tokenized_train]
        self.tweet_tokenized_test = [nltk.word_tokenize(x.lower()) for x in tweet_tokenized_test]
        
        
        