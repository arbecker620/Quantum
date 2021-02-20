import cirq


print(cirq.google.Sycamore)


a = cirq.NamedQubit("a")
b = cirq.NamedQubit("b")

circuit = cirq.Circuit(
    cirq.H(a),
    cirq.CNOT(a,b),
    cirq.measure(a,b)
)
print(circuit)


print("\nMoments in the circuit:\n")
for i, moment in enumerate(circuit):
    print('Moment {}: {}'.format(i,moment))

print(repr(circuit))

simulator = cirq.Simulator()


result = simulator.run(circuit, repetitions=10)

print(result)