import numpy as np
from tests import *


def is_square(A):
    if A.shape[0] == A.shape[1]:
        return True
    else:
        return False


def is_identity_matrix(A):
    if is_square(A) == True:
        diagonal_index = 0
        for rows in A:
            if rows[diagonal_index] != 1 or sum(rows) > 1:
                return False
            for elements in rows:
                if elements != 0 and rows[diagonal_index] != elements:
                    return False

            diagonal_index += 1

        return True

    else:
        return False


def matrix_transpose(A):
    return A.transpose()


def matrix_addition(A, B):
    if A.shape == B.shape:
        return A + B
    else:
        return f"ShapeError: A: {A.shape} B: {B.shape}"


def matrixes_multiplication(A, B):
    if A.shape[1] == B.shape[0]:
        return A * B
    else:
        return f"ShapeError: A: {A.shape[1]} != {B.shape[0]}"


def drop(M, col, row):
    M = np.delete(M, col, 1)
    M = np.delete(M, row, 0)
    return M


def det(A):
    result = 0
    if A.shape == (1, 1):
        return A[0][0]
    else:
        for i in range(len(A)):
            result += (A[0][i] * ((-1) ** (i + 2)) * det(drop(A, i, 0)))
        return result


def cofactor(A, col, row):
    return (-1) ** (col + row + 2) * det(drop(A, col, row))


# def matrix_trace(A):
#     pass
#
#
# def matrix_main_minor(A):
#     pass
#
#
# def matrix_leading_major_minors(A):
#     pass
#
# def matrix_minor(A):
#     pass
#
# def matrix_algebraic_complements(A, n, m):
#     pass
#
#
# def matrix_algebraic_complement(A):
#     pass
#
#
# def attached_matrix(A):
#     pass
#
#
# def matrix_inverse(A):
#     pass
#
#
# def is_diagonal_matrix():
#     pass
#
#
# def is_zero_matrix(A):
#     pass
