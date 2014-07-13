import sys
import json
import string

def normalize_text(text):
    return text.strip(string.punctuation + ' ').lower()

def get_states_dic():
    """Returns a dictionary of {state's abb : normalized state's name}.
    """
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
    output = {}
    for k in states.keys():
        output[normalize_text(k)] = normalize_text(states[k])
    return output

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

def tweet_state(tweet_json, state_dic):
    place = tweet_json.get('place')
    if place and place.get('country_code') == 'US':
        state_name, abb = place.get('full_name').split(',')
        state_name = normalize_text(state_name)
        abb = normalize_text(abb)
        ## Checks the simplest way, the state's abbreviation.
        if state_dic.has_key(abb):
            return abb
        ## Checks the city's name, which sometimes is the state's name (I 
        ## don't know why it happens).
        else:
            for k, v in state_dic.iteritems():
                if v == state_name:
                    return k
        return None

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dic = build_dictionary(sent_file)
    state_dic = get_states_dic()
    state_score = {}
    ## The score of each tweet is calculated and, if it's not zero, its State is
    ## found. The calculated score is used to calculate the overall State score.
    for tweet_line in tweet_file:
        tweet_json = json.loads(tweet_line)
        tweet_score = compute_tweet_score(tweet_json, sent_dic)
        if tweet_score != 0:
            state = tweet_state(tweet_json, state_dic)
            if state:
                n = state_score.get(state, 0)
                state_score[state] = n + tweet_score
    ## Finding the State with the higher sentiment score.
    maxv = - sys.maxint
    maxk = None
    for k, v in state_score.iteritems():
        if v > maxv:
            maxk = k
    print maxk.upper()


if __name__ == '__main__':
    main()
