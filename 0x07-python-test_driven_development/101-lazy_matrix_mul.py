#!/usr/bin/python3
"""My function lazy_matrix_mul  """
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Args:
            first parameter m_a
            second parameter m_b
       Return :
               A new matrix which is the  dot product of m_a and m_b

    """
    c = numpy.dot(m_a, m_b)
    return c

