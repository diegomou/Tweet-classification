import re
from nltk.tokenize import RegexpTokenizer


def find_URL(string): 
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url 

def find_hashtag(string):
    hashtag = re.findall(r'(#\w+)',string)
    return hashtag

def find_mention(string):
    label = re.findall(r"(@\w+)",string)
    return label

def find_apostrophe(string):
    apostrophes = list()
    apostrophes_1 = re.findall("[\w]+['][\w]+",string)
    apostrophes_2 = re.findall("[\w]+[´][\w]+",string)
    apostrophes.extend(apostrophes_1)
    apostrophes.extend(apostrophes_2)
    return apostrophes

def label_url(tweet):
    url = find_URL(tweet)
    if len(url) > 0:
        for i in range(len(url)):
            tweet = tweet.replace(url[i],'URL_label')
    else:
        pass        
    return tweet

def label_hashtag(tweet):
    hashtags = find_hashtag(tweet)
    N_hashtags = len(hashtags)
    if N_hashtags > 0:
        for i in range(N_hashtags):
            tweet = tweet.replace(hashtags[i],'hashtag_label')
    else:
        pass        
    return tweet

def label_mention(tweet):
    mentions = find_mention(tweet)
    N_mention = len(mentions)
    if N_mention > 0:
        for i in range(N_mention):
            tweet = tweet.replace(mentions[i],'mention_label')
    else:
        pass
        
    return tweet

def del_apostrophe(tweet):
    apostrophes = find_apostrophe(tweet)
    N_apostrophes = len(apostrophes)
    apostrophes_replacement = list()
    
    for i in range(N_apostrophes):
        if "'" in apostrophes[i]:
            apostrophes_replacement.append(apostrophes[i].replace("'",""))
        elif "´" in apostrophes[i]:
            apostrophes_replacement.append(apostrophes[i].replace("´",""))
        else:
            pass
    
    for i in range(N_apostrophes):
        tweet = tweet.replace(apostrophes[i],apostrophes_replacement[i])
    
    return tweet      