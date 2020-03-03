import re

def find_URL(string): 
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url 

def find_hashtag(string):
    hashtag = re.findall(r'(#\w+)',string)
    return hashtag

def find_mention(string):
    label = re.findall(r"(@\w+)",string)
    return label

def label_url(tweet):
    url = find_URL(tweet)
    if len(url) > 0:
        for i in range(len(url)):
            tweet = tweet.replace(url[i],'URL_label')
    else:
        pass        
    return tweet

def label_hashtag(tweet):
    url = find_hashtag(tweet)
    if len(url) > 0:
        for i in range(len(url)):
            tweet = tweet.replace(url[i],'hashtag_label')
    else:
        pass        
    return tweet

def label_mention(tweet):
    url = find_mention(tweet)
    if len(url) > 0:
        for i in range(len(url)):
            tweet = tweet.replace(url[i],'mention_label')
    else:
        pass
        
    return tweet