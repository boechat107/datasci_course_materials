import sys
import json
import string

## US States
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def normalize_text(text):
    return text.strip(string.punctuation).lower()

def build_dictionary(sent_file):
    dic = {}
    for line in sent_file:
        words, score = line.split('\t')
        dic[normalize_text(words)] = int(score)
    return dic

def compute_tweet_score(tweet_json, dic):
    content = tweet_json.get('text')
    score = 0
    if content:
        words = content.split()
        for w in words:
            w_score = dic.get(normalize_text(w))
            if w_score:
                score = score + w_score
    return score

def tweet_state(tweet_json):
    place = tweet_json.get('place')
    if place:
        print place.get('country')

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dic = build_dictionary(sent_file)
    state_dic = {}
    for tweet_line in tweet_file:
        tweet_json = json.loads(tweet_line)
        tweet_score = compute_tweet_score(tweet_json, sent_dic)
        if tweet_score != 0:
            state = tweet_state(tweet_json)

if __name__ == '__main__':
    main()
