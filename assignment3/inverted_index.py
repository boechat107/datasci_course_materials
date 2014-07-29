import sys
from MapReduce import MapReduce

mr = MapReduce()

def mapper(record):
    """
    record is a list of 2 items: [doc-name, text].
    """
    key = record[0]
    text = record[1]
    for w in text.split():
        mr.emit_intermediate(w, key)

def reducer(key, vals):
    """
    key is a word.
    vals is a list of doc-names.
    """
    mr.emit((key, list(set(vals))))


if __name__ == '__main__':
    data = open(sys.argv[1])
    mr.execute(data, mapper, reducer)
