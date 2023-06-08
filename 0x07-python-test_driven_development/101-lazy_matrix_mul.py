#!/usr/bin/python3

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    try:
        matrix_a = np.array(m_a)
        matrix_b = np.array(m_b)
        result = np.matmul(matrix_a, matrix_b)
        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
    except TypeError:
        raise TypeError("m_a and m_b must be lists of lists containing only integers or floats")

