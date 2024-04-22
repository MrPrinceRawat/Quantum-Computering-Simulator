from ast import Bytes
import random
import itertools
       

class qSystem:
    def __init__(self, size=3):
        self.q = [[0, 0, 1] for _ in range(size)]     

    def rotY90(self, b):
        x, y, z = self.q[b]
        # 90 deg rot on y axis
        if z == 1 and x == 0:
            self.q[b][0] += 1
            self.q[b][2] -= 1
        elif z == 0 and x == 1:
            self.q[b][0] -= 1
            self.q[b][2] -= 1
        elif z == -1 and x == 0:
            self.q[b][0] -= 1
            self.q[b][2] += 1
        elif z == 0 and x == -1:
            self.q[b][0] += 1
            self.q[b][2] += 1

    def rotX90(self, b):
        x, y, z = self.q[b]
        # 90 deg rot on y axis
        if z == 1 and y == 0:
            self.q[b][1] += 1
            self.q[b][2] -= 1
        elif z == 0 and y == 1:
            self.q[b][1] -= 1
            self.q[b][2] -= 1
        elif z == -1 and y == 0:
            self.q[b][1] -= 1
            self.q[b][2] += 1
        elif z == 0 and y == -1:
            self.q[b][1] += 1
            self.q[b][2] += 1

    def rotZ90(self, b):
        x, y, z = self.q
        # 90 deg rot on y axis
        if x == 1 and y == 0:
            self.q[b][0] -= 1
            self.q[b][1] -= 1
        elif x == 0 and y == -1:
            self.q[b][0] -= 1
            self.q[b][1] += 1
        elif x == -1 and y == 0:
            self.q[b][0] += 1
            self.q[b][1] += 1
        elif x == 0 and y == 1:
            self.q[b][0] += 1
            self.q[b][1] -= 1

    def X(self, b):
        self.rotX90(b)
        self.rotX90(b)
        return self.q[b]

    def Y(self, b):
        self.rotY90(b)
        self.rotY90(b)
        return self.q[b]

    def Z(self, b):
        self.rotZ90(b)
        self.rotZ90(b)
        return self.q[b]

    def getState(self):
        return self.q[b]


    def H(self, b):
        self.rotY90(b)
        self.rotX90(b)
        self.rotX90(b)
        return self.q[b]

    def CNOT(self, z, t):
        if z == 0:
            if random.randint(0, 1) == 1:
                self.X(t)
        elif z == -1:
            self.X(t)
        return

    def Measure(self, b):
        if self.q[b][-1] == 0:
            if random.randint(0, 1) == 0:
                self.q[b][-1] = 1
            else:
                self.q[b][-1] = -1
            self.q[b][0] = 0
        return self.q[b]

    def reset(self, b):
        self.q[b] = [0, 0, 1]


    def run(self, shots, circuit):
        possibleStates = 2 ** len(self.q)
        print(f"{possibleStates} Possible States\n\n")
        statesFound = []
        states = []
        MeasurementHistory = []
        for _ in range(shots):
            StateChangeHistory = []
            for l, i in enumerate(circuit):
                if i[0] == "H":
                    self.H(i[1])
                if i[0] == "X":
                    self.X(i[1])
                if i[0] == "Y":
                    self.Y(i[1])
                if i[0] == "Z":
                    self.Z(i[1])
                if i[0] == "CNOT":
                    # i[1] is the control qubit
                    # i[2] is the target qubit
                    self.CNOT(self.q[i[1]][2], i[2])
                if i[0] == "CZ":
                    self.H(i[1])
                    self.CNOT(self.Measure(i[2])[2], i[1])
                    self.H(i[1])
            qbitStates = []
            for i in range(len(self.q)):
                m = self.Measure(i)[2]
                if m == 1:
                    qbitStates.append(0)
                elif m == -1:
                    qbitStates.append(1)
                elif m == 0:
                    qbitStates.append(random.randint(0, 1))
                self.reset(i)
            MeasurementHistory.append(qbitStates)
        for i, z in enumerate(MeasurementHistory):
            if z not in states:
                statesFound.append([
                    round((MeasurementHistory.count(z) / shots) * 100, 2), z])
                states.append(z)
        statesFound.sort(key=lambda x: x[0], reverse=True)
        num = int(''.join(str(e) for e in statesFound[0][1]), 2)
        # print(len(str(num)))
        # print(num)
        # print("\n")
        for i in statesFound:
            if i[0] != 0:
                print(i)


# def run(s, shots):
#     possibleStates = 2 ** len(s)
#     print(f"{possibleStates} Possible States")
#     states = list(itertools.product([0, 1], repeat=len(s)))
#     statesFound = [0 for _ in range(possibleStates)]
#     MeasurementHistory = []
#     for _ in range(shots):
#         qbitStates = []
#         for i in s:
#             m = i.Measure()[2]
#             if m == 1:
#                 qbitStates.append(0)
#             elif m == -1:
#                 qbitStates.append(1)
#             elif m == 0:
#                 qbitStates.append(random.randint(0, 1))
#         MeasurementHistory.append(qbitStates)
#     for i, z in enumerate(states):
#         statesFound[i] = [
#             round((MeasurementHistory.count(list(z)) / shots) * 100, 2), str(z)]
#     statesFound.sort(key=lambda x: x[0], reverse=True)
#     for i in statesFound:
#         if i[0] != 0:
#             print(i)
