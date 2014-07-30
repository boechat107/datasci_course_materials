import sys
from MapReduce import MapReduce

mr = MapReduce()

def ordered_tuple(a, b):
    out = None
    if a < b:
        out = (a, b)
    else:
        out = (b, a)
    return out

def mapper(record):
    """
    record is a 2 element list [personA, personB]
    """
    personA = record[0]
    personB = record[1]
    key = ordered_tuple(personA, personB)
    mr.emit_intermediate(key, personB)

def reducer(key, vals):
    """
    key is a set of (personA, personB).
    vals is the list of personB.
    """
    if len(vals) == 1:
        mr.emit((key[0], key[1]))
        mr.emit((key[1], key[0]))


if __name__ == '__main__':
    data = open(sys.argv[1])
    mr.execute(data, mapper, reducer)
