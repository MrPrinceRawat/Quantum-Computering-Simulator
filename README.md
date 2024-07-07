# Quantum Computer Simulator

![GitHub branch status](https://img.shields.io/github/checks-status/MrPrincerawat/Quantum-Computering-Simulator/pypi_release)
![PyPI - License](https://img.shields.io/pypi/l/simple_qsim)
![PyPI - Status](https://img.shields.io/pypi/status/simple_qsim)
![PyPI - Version](https://img.shields.io/pypi/v/simple_qsim)

### Headover to [PyPi](https://pypi.org/project/simple-qsim/) to install the package, relevent docs available at [ReadTheDocs](https://simple-qsim.readthedocs.io/en/latest/)

This is a simple project to simulate quantum behaviour on your local machine. One of the benefit of running this locally is there is essentially no limit on how many qubits can scale too, it comes down to your PC's specs and how many qubits you as a person handle.

# How to use

1. Clone this repo
2. There are basically 2 file
   a. Gates.py - Holds all the logic
   b. Main.py - This is where you write your code.
3. Sample main.py

```
import numpy as np
from gates import *
import time

# Register number of qubits you want to use.
s = [
q() for _ in  range(3)
]
# Sample Circuit
c = [
["H", s[0]],
["H", s[1]],
["H", s[2]],
["Z", s[2]],
["CZ", s[0], s[1]],
["H", s[0]],
["H", s[1]],
["H", s[2]],
]
run(s, shots=10000, circuit=c)
```

4. Then run it using python
   `python3 main.py`
5. You should see something like:

```
8 Possible States


[25.85, [0, 1, 1]]
[25.07, [1, 0, 1]]
[24.77, [1, 1, 1]]
[24.31, [0, 0, 1]]
```

You can verify or use the GUI on IBM's platform here: [IBM Quantum Composer](https://quantum.ibm.com/composer/)

# Available Gates

You can learn more about quantum gates at [Wikipeida](https://en.wikipedia.org/wiki/Quantum_logic_gate)

1. Single Qubit Gates

````
	a. Hadamard Gate (H)
		Puts the qubit in super position
		Use - ```["H", q[n]]```
	b. Pauli Gates (X,Y,Z)
		Spins the qubit 90deg in that axis
		Use - ["X", q[n]]
			  ["Y", q[n]]
			  ["Z", q[n]]
````

2. Controlled Gates

```
	a. Controlled-NOT (CNOT)
		Performs a not operation on targed when the control bit is |1⟩
		Use - ["CNOT", <target>, <control>]
	b. Controlled-Z (CZ)
		Performs a Pauli Z operation on targed when the control bit is |1⟩
		Use - ["CZ", <target>, <control>]
```

# Contribution

I might or might not update this repo myself, however I am open to contribution!

# License

All the code available in this repo is under apache 2.0 license.
