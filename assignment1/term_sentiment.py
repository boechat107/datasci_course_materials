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

def print_new_dictionary(new_dic):
    for w, counters in new_dic.iteritems():
        if counters[1] == 0:
            print w, counters[0]
        else:
            print w, counters[0] / counters[1]


## To calculate the sentiment of the terms that do not appear in the sentiment file,
## we can divide the number of occurrences in positive tweets by the number of 
## occurrences in negative tweets.
## 
## term_score = N of positive tweets 
##              --------------------
##              N of negative tweets

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dic = build_dictionary(sent_file)
    ## New dictionary with words that don't appear in the given sentiment file.
    new_dic = {}
    for tweet_line in tweet_file:
        words = tweet_words(tweet_line)
        if words:
            tweet_score = compute_tweet_score(words, sent_dic)
            ## Counts positive and negative occurrences of some words.
            for w in words:
                if not sent_dic.has_key(w) or tweet_score != 0:
                    np, nn = new_dic.get(w, (0,0))
                    ## The tuple is composed of (N positive, N negative).
                    if tweet_score > 0:
                        np = np + 1
                    else:
                        nn = nn + 1
                    new_dic[w] = (np, nn)
    print_new_dictionary(new_dic)

if __name__ == '__main__':
    main()
