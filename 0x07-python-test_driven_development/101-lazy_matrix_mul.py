#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        numpy.ndarray: Result of matrix multiplication.

    Raises:
        ValueError: If m_a or m_b is empty or if matrices cannot be multiplied.
    """

    try:
        result = np.dot(m_a, m_b)
        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")

if __name__ == "__main__":
    # You can add test cases here or use the provided 101-main.py script for testing
    pass

