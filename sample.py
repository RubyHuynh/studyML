from scipy import sparse

eye = np.eye(4)
print ("numPy array: \n {}" . format(eye))
sparse_matrix = sparse.csr_matrix(eye)
print ("\n Scipy sparse CSR matrix: \n{}".format(sparse_matrix))
