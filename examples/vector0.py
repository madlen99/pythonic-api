'''
Vector: classe vetor euclideano

    >>> v1 = Vector([1, 2])
    >>> v1
    Vector([1.0, 2.0])

'''

from array import array 
import math

class Vector:

    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)
    
    def __len__(self):
        return len(self._components)

    def __iter__(self):
        return iter(self._components)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __eq__(self, other):
        return (len(self) == len(other) and
            all(a == b for a, b in zip(self, other)))

    def __repr__(self):
        return 'Vector({})'.format(list(self._components))
