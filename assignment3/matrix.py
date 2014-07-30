import sys
from MapReduce import MapReduce

mr = MapReduce()

## Although the problem description didn't say that, the matrices' sizes must be
## known. The sizes below were inferred from the data set file.
## size(A) = L x M
## size(B) = M x N
L = 5
M = 5
N = 5

def mapper(record):
    """
    record is a 4 element list [matrix, i, j, value]
    """
    mat, i, j, value = record 
    if mat == 'a':
        ## For A, each element can be used for all columns of the matrix B.
        for k in range(N):
            mr.emit_intermediate((i, k), record)
    else:
        ## For B, each element can be used for all rows of the matrix A.
        for l in range(L):
            mr.emit_intermediate((l, j), record)

def reducer(key, vals):
    """
    key is element position (i,j)
    vals is the list of matrix element records.
    """
    mat_a = {}
    mat_b = {}
    ## First we map the column indexes of A elements and the row indexes of B
    ## elements.
    for r in vals:
        mat, i, j, v = r
        if mat == 'a':
            mat_a[j] = v
        else:
            mat_b[i] = v
    ## Now we can try to match the indexes for the multiplication.
    elem_sum = 0
    for j in mat_a.keys():
        if mat_b.has_key(j):
            elem_sum += mat_a[j] * mat_b[j]
    mr.emit((key[0], key[1], elem_sum))


if __name__ == '__main__':
    data = open(sys.argv[1])
    mr.execute(data, mapper, reducer)
