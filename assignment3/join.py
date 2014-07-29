import sys
from MapReduce import MapReduce

mr = MapReduce()

def mapper(record):
    """
    record is a list containing a lot of attributes, but the first (table name) and
    the second (order id) are the most important for this problem.
    """
    table = record[0]
    orderId = record[1]
    mr.emit_intermediate(orderId, record)

def reducer(key, vals):
    """
    key is the order id.
    vals is the list of records whose order id is equal to key.
    """
    categs = {}
    ## Grouping the records by the table name.
    for r in vals:
        tname = r[0]
        tlist = categs.get(tname, [])
        tlist.append(r)
        categs[tname] = tlist
    ## Combining records of different categories.
    for r1 in categs['order']:
        for r2 in categs['line_item']:
            ## Concatenates the two records.
            mr.emit(r1 + r2)


if __name__ == '__main__':
    data = open(sys.argv[1])
    mr.execute(data, mapper, reducer)
