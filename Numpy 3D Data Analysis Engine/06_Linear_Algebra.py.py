import numpy as np
data=np.load("datasets/sensor_data.npy")
temperature=data[:,:,0]
print(temperature.shape)
transposed_temperature=temperature.transpose()
print(transposed_temperature.shape)
humidity=data[:,:,1]
print(humidity.shape)
transposed_humidity=humidity.transpose()
print(transposed_humidity.shape)
result_1=temperature@transposed_humidity
result_2=np.matmul(temperature,transposed_humidity)
result_3=np.dot(temperature,transposed_humidity)
print(np.array_equal(result_1,result_2))
print(np.array_equal(result_2,result_3))
A=np.array([[4, 2],
              [3, 1]])
inverse = np.linalg.inv(A)
print(A@inverse)
B=np.array([[2,1],
            [1,1]])
determinant=np.linalg.det(B)
inverse_B=np.linalg.inv(B)
print(B@inverse_B,'\n',determinant)
B=np.array([[2,1],
            [1,1]])
determinant=np.linalg.det(B)
inverse_B=np.linalg.inv(B)
print(B@inverse_B,'\n',determinant)
C = np.array([
    [4, 2],
    [2, 3]])
egval,egvec=np.linalg.eig(C)
print("Eigenvalues:",egval)
print("Eigenvectors:",egvec)
left=C@egvec
right=egvec*egval
print(np.allclose(left, right))

