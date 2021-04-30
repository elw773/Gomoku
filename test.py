%%cython
def f(n):
    a = 0
    for i in range(n):
        a += i
        return a

cpdef g(int n):
    cdef long a = 0
    cdef int i
    for i in range(n):
        a += i
        return a
