import numpy as np
from gates import *
import time
import resource
import itertools

# resource.setrlimit(resource.RLIMIT_AS, (2147483648, 2147483648))

s = [
    q() for _ in range(3)
]

# Simple 3 Qubit, entangled, circuit expirement.
c = [
    ["H", s[0]],
    ["H", s[1]],
    ["H", s[2]],
    # #! LEVEL 2
    ["Z", s[2]],
    ["CZ", s[0], s[1]],
    #! LEVEL 3
    ["H", s[0]],
    ["H", s[1]],
    ["H", s[2]],
]


# c = [
#     ["H", s[0]],
#     ["H", s[1]],
#     ["CNOT", s[1], s[0]],
#     ["H", s[0]]
# ]

# c = [
#     ["H", s[0]],
#     ["H", s[1]],
#     ["CZ", s[0], s[1]],
#     ["H", s[0]],
#     ["H", s[1]],
#     ["z", s[0]],
#     ["z", s[1]],
#     ["CZ", s[0], s[1]],
#     ["H", s[0]],
#     ["H", s[1]],
# ]

# c = [
#     ["H", s[x]] for x in range(4098)
# ]

start = time.time()
run(s, shots=10000, circuit=c)
end = time.time()

# print("Time took>", end - start)
