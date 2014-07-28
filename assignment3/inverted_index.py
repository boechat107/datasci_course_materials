import sys
from MapReduce import MapReduce

class InvertedIndex(object):

    mr = None

    def mapper(self, record):
        """
        record is a list of 2 items: [doc-name, text].
        """
        key = record[0]
        text = record[1]
        for w in text.split():
            self.mr.emit_intermediate(w, key)

    def reducer(self, key, vals):
        """
        key is a word.
        vals is a list of doc-names.
        """
        self.mr.emit((key, list(set(vals))))

    def solve(self, data):
        self.mr = MapReduce()
        self.mr.execute(data, self.mapper, self.reducer)


if __name__ == '__main__':
    data = open(sys.argv[1])
    inverted_index = InvertedIndex()
    inverted_index.solve(data)
