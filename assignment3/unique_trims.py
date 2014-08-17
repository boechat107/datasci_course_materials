import sys
from MapReduce import MapReduce

mr = MapReduce()

def mapper(record):
    """
    record is a 2 element list [sequence id, nucleotides]
    """
    seqid = record[0]
    nucleotides = record[1]
    mr.emit_intermediate(nucleotides[0:-10], seqid)

def reducer(key, vals):
    """
    key is a string of nucleotides
    vals is the list of seqids.
    """
    mr.emit(key)


if __name__ == '__main__':
    data = open(sys.argv[1])
    mr.execute(data, mapper, reducer)
