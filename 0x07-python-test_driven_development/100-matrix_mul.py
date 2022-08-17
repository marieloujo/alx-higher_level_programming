#!/usr/bin/python3
"""Module that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Muttiplies 2 matrices

    Args:
        m_a (list of list): first matrice
        m_b (list of list): second matrice

    Return:
        New matrice of (n*p) for:
            n 
    """
    my_matrix = []
    if is_valid_matrice(m_a, "m_a") and is_valid_matrice(m_b, "m_b"):
        my_matrix = [[sum := sum + (col_a * col_b for col_b in row_b) for col_a in row_a] for row_a in m_a for row_b in zip(*m_b)]
        """ for row_a in m_a and row_b in zip(*m_b):
            row = []
            for col_a in row_a:
                sum = 0
                for col_b in row_b:
                    print("{} * {}".format(col_a, col_b))
                    sum += col_a * col_b
                print()
            row.append(sum)
        my_matrix.append(row) """
        """return [[col_a for col_a in _a] for _a in m_a ]"""
        """ return [[col_b for col_b in row_b] for row_b in zip(*m_b)] """
        return my_matrix

def is_valid_matrice(matrix, matrixName):
    """
    Check if matrice is valid

    Args:
        matrix (list of list): first matrice
        matrixName (str): contain name of matrice

    Return
        True|False
    """
    if type(matrix) is not list:
        raise TypeError(matrixName + " must be a list")
    if len(matrix) == 0:
        raise TypeError(matrixName + " can't be empty")
    if len(matrix) == 1:
        if len(matrix[0]) == 0:
            raise TypeError(matrixName + " can't be empty")
    for row in matrix:
        if type(row) is not list:
            raise TypeError(matrixName + "must be a list of lists")
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError(matrixName + "should contain only integers or floats")
    if len(matrix) > 0:
        if any(len(lst) != len(matrix[0]) for lst in matrix[1:]):
            raise TypeError("each row of "+ matrixName + " must be of the same size")
    return True


print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))