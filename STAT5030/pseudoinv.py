import numpy as np
import scipy

# Generate orthonormal vectors
def GenOrthVec(UT: np.array):
    mat_shape = UT.shape[0]
    rawgram = np.random.dirichlet(tuple([1 for i in range(mat_shape)]))
    rawgram /= scipy.linalg.norm(rawgram)
    gram = rawgram - np.dot(rawgram, UT[0]) * UT[0]

    for i in range(1, mat_shape):
        gram -= np.dot(gram, UT[i]) * UT[i]
    gram /= scipy.linalg.norm(gram)
    
    return gram

# Generate the Moore-Penrose Inverse
def GenMPInv(mat: np.array):
    mat_shape = mat.shape

    if mat_shape[1] > mat_shape[0]: # if the number of columns are greater than the number of rows
        mat = mat.transpose()
        mat_shape = mat.shape

    eigenval, eigenvec = np.linalg.eigh(np.matmul(mat.transpose(), mat))
    eigenvec = eigenvec[np.argsort(eigenval)[::-1]].transpose()
    eigenval = np.sort(eigenval)[::-1]
    
    svd_left = np.matmul(mat, eigenvec)

    S = np.zeros(mat_shape)
    for i in range(len(eigenval)):
        S[i][i] = np.sqrt(eigenval[i])

    UT = np.zeros((mat_shape[0], mat_shape[0]))
    for i in range(len(eigenval)):
        if eigenval[i] > 0:
            u = svd_left.transpose()[i] / S[i][i]
            UT[i] = u

    for i in range(mat_shape[0]):
        if scipy.linalg.norm(UT[i]) == 0.0:
            UT[i] = GenOrthVec(UT)

    SP = np.zeros((S.shape[1], S.shape[0]))
    for i in range(len(eigenval)):
        if eigenval[i] > 0:
            SP[i][i] = 1 / np.sqrt(eigenval[i])

    MPInv = np.matmul(eigenvec.transpose(), SP)
    MPInv = np.matmul(MPInv, UT)
    MPInv = np.abs(MPInv)

    return MPInv

# Generate the Generalized Inverse
def GenGInv():
    return 1


if __name__ == "__main__":
    mat = np.array([[2, 6], [1, 3], [3, 9], [5, 15]])
    print(GenMPInv(mat))
