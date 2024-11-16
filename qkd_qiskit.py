import random
from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit

simulator = AerSimulator()

n_qubits = 5

def generate_alice_choices(n):
    bits = [random.randint(0, 1) for _ in range(n)]  # Random bits (0 or 1)
    bases = [random.choice(['computational', 'diagonal']) for _ in range(n)]  # Random bases
    return bits, bases

def generate_bob_bases(n):
    return [random.choice(['computational', 'diagonal']) for _ in range(n)]

def simulate_qkd(n_qubits):
    alice_bits, alice_bases = generate_alice_choices(n_qubits)
    
    bob_bases = generate_bob_bases(n_qubits)
    
    qc = QuantumCircuit(n_qubits, n_qubits)
    
    for i in range(n_qubits):
        if alice_bases[i] == 'diagonal':  # Diagonal basis -> apply Hadamard
            qc.h(i)
        
        if alice_bits[i] == 1:  # Flip qubit for bit 1
            qc.x(i)
    
    for i in range(n_qubits):
        if bob_bases[i] == 'diagonal':  # Diagonal basis -> apply Hadamard
            qc.h(i)
        
        qc.measure(i, i)  # Measure the qubit
    
    result = simulator.run(qc, shots=10000, memory=True).result()
    bob_bits = [int(bit) for bit in result.get_memory()[0]]  # Bob's measurement outcomes
    
    # Compare bases and extract the key
    key = []
    matched_indices = []
    mismatched_indices = []
    
    for i in range(n_qubits):
        if alice_bases[i] == bob_bases[i]:  # Basis match
            if alice_bits[i] == bob_bits[i]:  # Bits also match
                key.append(alice_bits[i])  # Add the bit to the key
                matched_indices.append(i)  # Store index of the matched bit
            else:
                mismatched_indices.append(i)  # Store index of the mismatched bit
        else:
            mismatched_indices.append(i)  # Store index of the mismatched bases
    
    return {
        "alice_bits": alice_bits,
        "alice_bases": alice_bases,
        "bob_bases": bob_bases,
        "bob_bits": bob_bits,
        "matched_indices": matched_indices,
        "mismatched_indices": mismatched_indices,
        "key": key,
    }

result = simulate_qkd(n_qubits)

print("\n--- QKD Simulation Details ---")
print(f"Alice's Bits:        {result['alice_bits']}")
print(f"Alice's Bases:       {result['alice_bases']}")
print(f"Bob's Bases:         {result['bob_bases']}")
print(f"Bob's Bits:          {result['bob_bits']}")
print("\nMatched Indices:     ", result["matched_indices"])
print("Mismatched Indices:  ", result["mismatched_indices"])
print("\nFinal Key:           ", ''.join(map(str, result["key"])))
