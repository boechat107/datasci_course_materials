import sys
import json
import string

def normalize_text(text):
    return text.strip(string.punctuation).lower()

def tweet_words(tweet_line):
    """Split a tweet line into words, normalizing each one. This function can return
    None if the text field doesn't exist in the tweet line.
    """
    tweet_content = json.loads(tweet_line).get('text')
    if tweet_content:
        return [normalize_text(w) for w in tweet_content.split()]
    else:
        return None

def print_words_counter(dic, ntotal_words):
    for w, nw in dic.iteritems():
        print w, float(nw) / ntotal_words

def main():
    tweet_file = open(sys.argv[1])
    ntotal_words = 0
    words_counter = {}
    for tweet_line in tweet_file:
        words = tweet_words(tweet_line)
        if words:
            ntotal_words = ntotal_words + len(words)
            for w in words:
                nw = words_counter.get(w, 0)
                words_counter[w] = nw + 1
    print_words_counter(words_counter, ntotal_words)

if __name__ == '__main__':
    main()
