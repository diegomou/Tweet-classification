import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


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
        
        self.tweet_tokenized_train = None
        self.tweet_tokenized_test = None
    
    def load_data(self):
        self.raw_train = pd.read_csv('train.csv')
        self.raw_test = pd.read_csv('test.csv')
        
        self.target_train = self.raw_train.target
        self.raw_tweet_train = self.raw_train.text
        self.raw_tweet_test = self.raw_test.text
       
    def prepro_tweets(self):
        self.tweet_prepro_train = [f_NLP.label_url(x) for x in self.raw_tweet_train]
        self.tweet_prepro_test = [f_NLP.label_url(x) for x in self.raw_tweet_test]
        
        self.tweet_prepro_train = [f_NLP.label_hashtag(x) for x in self.tweet_prepro_train]
        self.tweet_prepro_test = [f_NLP.label_hashtag(x) for x in self.tweet_prepro_test]
        
        self.tweet_prepro_train = [f_NLP.label_mention(x) for x in self.tweet_prepro_train]
        self.tweet_prepro_test = [f_NLP.label_mention(x) for x in self.tweet_prepro_test]
        
        self.tweet_prepro_train = [f_NLP.del_apostrophe(x) for x in self.tweet_prepro_train]
        self.tweet_prepro_test = [f_NLP.del_apostrophe(x) for x in self.tweet_prepro_test]
        
    def tokenizer(self):      
        """
        The tokenizer funtion tokenize and remove punctuation using the NLTK's
        RegexpTokenizer. This tokenizer use a regular expresion in the tokenize
        process, deleting the punctuation.
        """
        tokenizer = RegexpTokenizer(r'\w+')
        
        self.tweet_tokenized_train = [tokenizer.tokenize(x.lower()) for x in self.tweet_prepro_train]
        self.tweet_tokenized_test = [tokenizer.tokenize(x.lower()) for x in self.tweet_prepro_test]   
        
    def filtro_stopwords(self,lista_a_retener = []):
        
        if len(lista_a_retener) == 0:
            stopwords_list = stopwords.words('english')
        else:
            stopwords_list = [x for x in stopwords.words('english') if (x in lista_a_retener) == False]
        
        for i in range(len(self.tweet_tokenized_train)):
            self.tweet_tokenized_train[i]= [x for x in self.tweet_tokenized_train[i] if (x in stopwords_list) == False]
            
        for j in range(len(self.tweet_tokenized_test)):
            self.tweet_tokenized_test[j]= [x for x in self.tweet_tokenized_test[j] if (x in stopwords_list) == False]    