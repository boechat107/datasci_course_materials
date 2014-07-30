import sys
from MapReduce import MapReduce

mr = MapReduce()

def mapper(record):
    """
    record is a 2 element list [personA, personB]
    """
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate(personA, personB)

def reducer(key, vals):
    """
    key is a personA.
    vals is the list of personB.
    """
    count = 0
    for p in vals:
        count += 1
    mr.emit((key, count))


if __name__ == '__main__':
    data = open(sys.argv[1])
    mr.execute(data, mapper, reducer)
