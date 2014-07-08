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

def compute_tweet_score(tweet_line, dic):
    tweet_json = json.loads(tweet_line)
    content = tweet_json.get('text')
    score = 0
    if content:
        words = content.split()
        for w in words:
            w_score = dic.get(normalize_text(w))
            if w_score:
                score = score + w_score
    return score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dic = build_dictionary(sent_file)
    for tweet_line in tweet_file:
        print compute_tweet_score(tweet_line, sent_dic)

if __name__ == '__main__':
    main()
