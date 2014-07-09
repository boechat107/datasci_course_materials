import sys
import json
import string

def normalize_text(text):
    return text.strip(string.punctuation).lower()

def build_dictionary(sent_file):
    dic = {}
    for line in sent_file:
        words, score = line.split('\t')
        dic[normalize_text(words)] = int(score)
    return dic 

def tweet_words(tweet_line):
    """Split a tweet line into words, normalizing each one. This function can return
    None if the text field doesn't exist in the tweet line.
    """
    tweet_content = json.loads(tweet_line).get('text')
    if tweet_content:
        return [normalize_text(w) for w in tweet_content.split()]
    else:
        return None

def compute_tweet_score(words, dic):
    score = 0
    for w in words:
        w_score = dic.get(w)
        if w_score:
            score = score + w_score
    return score

def print_words_sentiment(content, dic, tweet_score):
    pass

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dic = build_dictionary(sent_file)
    for tweet_line in tweet_file:
        words = tweet_words(tweet_line)
        if words:
            tweet_score = compute_tweet_score(words, sent_dic)
            print tweet_score

if __name__ == '__main__':
    main()
