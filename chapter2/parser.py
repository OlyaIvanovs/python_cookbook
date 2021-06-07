# Parse text according to a set of grammar rules and perform actions
# or build an abstract syntax tree representing the input.

import time
import cProfile


def addUpNumbers():
    total = 0
    for i in range(1, 1000001):
        total += i


cProfile.run('addUpNumbers()')
