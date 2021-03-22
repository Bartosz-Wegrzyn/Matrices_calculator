# This Python script is a basics matrices calculator, just for my practice peres to understand how matrices works.

import numpy as np


### auxiliary definitions ###

def is_identity_matrix():
    pass


def is_diagonal_matrix():
    pass


def zero_matrix(A):
    pass


### Main definicions ###

def matrix_transpose(A):
    out = np.array()


def matrix_addition(A, B):
    if A.shape == B.shape:
        return A + B
    else:
        return f"ShapeError: A: {A.shape} B: {B.shape}"


def matrix_multiplication(A, B):
    if A.shape[1] == B.shape[0]:
        return A * B
    else:
        return f"ShapeError: A: {A.shape} B: {B.shape} \n            {A.shape[1]} != {B.shape[0]}"


def matrix_determinant(A):
    pass


def matrix_trace(A):
    pass


# def matrix_main_minor(A):
#     pass


# def matrix_leading_major_minors(A):
#     pass

# def matrix_minor(A):
#     pass

def matrix_algebraic_complements(A, n, m):
    pass


def matrix_algebraic_complement(A):
    pass


def attached_matrix(A):
    pass


def matrix_inverse(A):
    pass


### Test arrays ###

A = np.array([[1, 0, 4, 9, 10, 11, 77]])

B = np.array([
    [0, 2, 3, 2, 12],
    [0, 4, 1, 1, 2],
    [0, 32, 1, 11, 2],
    [0, 4, 2, 11, 1],
    [12, 0, 4, 3, 9]])

C = np.array([
    [1, 2],
    [2, 2],
    [9, 1],
    [3, 0]])

D = np.array([
    [12],
    [3],
    [14],
    [23]])

E = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]])

F = np.array([
    [1, 0, 0],
    [0, 4, 0],
    [0, 0, 4]])

G = np.array([
    [0, 4, 1, 1],
    [1, 0, 4, 0]])

print(matrix_multiplication(A, C))
