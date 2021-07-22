import numpy as np
from tests import *


def is_square(A):
    if A.shape[0] == A.shape[1]:
        return True
    else:
        return False


def is_identity(A):  # Macierz jednostkowa
    if is_square(A):
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


def transpose(A):
    a, b = A.shape
    out = np.zeros((b, a), dtype=int)
    for i in range(len(A)):

        for j in range(len(A[0])):
            out[j][i] = A[i][j]
    return out


def addition(A, B):
    if A.shape == B.shape:
        return A + B
    else:
        return f"ShapeError: A: {A.shape} B: {B.shape}"


def substraction(A, B):
    if A.shape == B.shape:
        return A - B
    else:
        return f"ShapeError: A: {A.shape} B: {B.shape}"


def multiplication(A, B):
    if A.shape[1] == B.shape[0]:
        return A @ B
    else:
        return f"ShapeError: A: {A.shape[1]} != {B.shape[0]}"


def drop(M, col, row):
    M = np.delete(M, col, 1)
    M = np.delete(M, row, 0)
    return M


def det(A):  # Wyznacznik Macierzy
    result = 0
    if A.shape == (1, 1):
        return A[0][0]
    else:
        for i in range(len(A)):
            result += (A[0][i] * ((-1) ** (i + 2)) * det(drop(A, i, 0)))
        return result


def cofactor(A, col, row):  # Dopełnienie Algebraiczne
    return (-1) ** (col + row + 2) * det(drop(A, col, row))


def trace(A):
    out = 0
    if is_square(A):
        for i in range(len(A)):
            out += A[i][i]
        return out


def cofactor_matrix(J):  # maciez_dopelnien_algebraicznych:
    out = np.zeros(J.shape, dtype=int)
    for i in range(len(J)):
        for j in range(len(J)):
            out[j][i] = cofactor(J, i, j)
    return out


def adjugate_matrix(A):  # Maciez dołączona
    return transpose(cofactor_matrix(A))


def inverse_matrix(A):
    return adjugate_matrix(A) / det(A)
