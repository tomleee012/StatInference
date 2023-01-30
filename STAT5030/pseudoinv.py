import numpy as np
import scipy

#  Generate the Moore-Penrose Inverse
def GenMPInv(mat: np.array):
    mat_shape = mat.shape

    # if the number of columns are greater than the number of rows
    if mat_shape[1] > mat_shape[0]:
        # rank(mat) <= rows
        mat_sq = np.matmul(mat, mat.transpose()) # mat_sq = A A^T
        eigenval, eigenvec = np.linalg.eig(mat_sq)
        eigenval = np.sort(eigenval)[::-1]

        # singular matrix S
        S = np.zeros(mat_shape)
        for i in range(len(eigenval)):
            S[i][i] = np.sqrt(eigenval[i])

        # singular value decomposition
        svd_left = np.matmul(mat, eigenvec.transpose()) # AV = US

        # matrix U
        UT = np.zeros((mat_shape[1], mat_shape[1]))
        for i in range(len(eigenval)):
            if eigenval[i] > 0:
                u = svd_left.transpose()[i]
                UT[i] = u

    # if the number of rows are greater than the number of columns
    else:
        # rank(mat) <= columns
        mat_sq = np.matmul(mat.transpose(), mat) # mat_sq = A^T A
        eigenval, eigenvec = np.linalg.eig(mat_sq)
        eigenval = np.sort(eigenval)[::-1]
        # singular matrix S
        # singular value decomposition
        ds

    return 1

# Generate the Generalized Inverse
def GenGInv():
    return 1


if __name__ == "__main__":
    results = GenMPInv()
