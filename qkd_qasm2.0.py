# OPENQASM 2.0;
# include "qelib1.inc";

# qreg q[5];                
# creg alice_bits[5];       
# creg bob_bits[5];    

# x q[0];                    
# h q[0];                    
# h q[1];                    
# x q[2];                    

# x q[3];                    
# h q[3];                    


# h q[4];                   

# //h q[0];                    // Diagonal basis (remove this line for computational basis)
# measure q[0] -> bob_bits[0];

# measure q[1] -> bob_bits[1]; // Computational basis

# //h q[2];                    // Diagonal basis
# measure q[2] -> bob_bits[2];

# measure q[3] -> bob_bits[3]; // Computational basis

# //h q[4];                    // Diagonal basis
# measure q[4] -> bob_bits[4];
# measure q[0] -> alice_bits[0];
# measure q[1] -> alice_bits[1];
# measure q[2] -> alice_bits[2];
# measure q[3] -> alice_bits[3];
# measure q[4] -> alice_bits[4];
