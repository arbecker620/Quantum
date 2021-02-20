import cirq
import numpy as np
from cirq import Circuit
from cirq.devices import GridQubit
from cirq.google import XmonDevice


length = 6
#create number of quibits
qubits = [cirq.GridQubit(x, y) for x in range(length) for y in range(length)]
print(qubits)



#create circuit
circuit = cirq.Circuit()



#assigning haradrian gates
H_1 = cirq.H(qubits[2])
TOFFOLIO = cirq.TOFFOLI(qubits[2], qubits[3], qubits[4])
H_2 = cirq.H(qubits[1])
H_3 = cirq.H(qubits[2])
H_4 = cirq.H(qubits[3])

CZ1 = cirq.CZ(qubits[2], qubits[1])
CZ2 = cirq.CZ(qubits[2], qubits[3])


moment1 = cirq.Moment([H_1])
moment2 = cirq.Moment([TOFFOLIO])
moment3 = cirq.Moment([H_1])
moment4 = cirq.Moment([H_2, H_3, H_4])
moment5 = cirq.Moment([CZ1])
moment6 = cirq.Moment([CZ2])
moment7 = cirq.Moment([H_2, H_3, H_4])

circuit = cirq.Circuit((moment1, moment2, moment3, moment4, moment5, moment6, moment7 ))

print(circuit)
simulator = cirq.Simulator()
result = simulator.simulate(circuit)
print(result)
