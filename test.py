import numpy as np
from gatesv2 import *
import time

s = qSystem(4098)

# Simple 3 Qubit, entangled, circuit expirement.
# c = [
#     ["H", 0],
#     ["H", 1],
#     ["H", 2],
#     # #! LEVEL 2
#     ["Z", 2],
#     ["CZ", 0, 1],
#     #! LEVEL 3
#     ["H", 0],
#     ["H", 1],
#     ["H", 2],
# ]


# c = [
#     ["H", 0],
#     ["H", 1],
#     ["CNOT", 0, 1],
#     ["H", 0]
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

c = [
    ["H", x] for x in range(4098)
]

start = time.time()
s.run(shots=100, circuit=c)
end = time.time()

print("Time took>", end - start)
