import sys
import json
import string
import operator

def get_hashtags(tweet_json):
    if tweet_json.has_key('entities'):
        return map(operator.itemgetter('text'), tweet_json.get('entities').get('hashtags'))
    return None

def top_k(tcounter, k):
    """Sorts the given map by value and returns the top k keys as tuples (k, v).
    """
    sorted_tuples = sorted(tcounter.iteritems(), key=operator.itemgetter(1))
    n_to_pop = min(k, len(sorted_tuples))
    return [sorted_tuples.pop() for i in range(n_to_pop)]

def main():
    tweet_file = open(sys.argv[1])
    htags_counter = {}
    for tweet_line in tweet_file:
        tweet_json = json.loads(tweet_line)
        hashtags = get_hashtags(tweet_json)
        if hashtags:
            for ht in hashtags:
                nht = htags_counter.get(ht, 0)
                htags_counter[ht] = nht + 1
    top10_tuples = top_k(htags_counter, 10)
    for ht, n in top10_tuples:
        print ht, n


if __name__ == '__main__':
    main()
