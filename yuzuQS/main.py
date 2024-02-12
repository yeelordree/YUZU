import numpy as np

class QC:
    def __init__(self, num_qbits):
        self.n = num_qbits
        self.state = np.zeros(2**self.num_qbits, dtype=np.complex128)

        # Initialize the quantum state to be proper, ie the vector [1, 0] which is the quantum
        # state 0.
        self.state[0] = 1
    
