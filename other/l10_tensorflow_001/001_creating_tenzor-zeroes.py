import tensorflow as tf
import tensorflow.keras. initializers as inits

initializers_zeros = inits.Zeros()

t_matrix = initializers_zeros((3, 3))
print(t_matrix)

t_vector = initializers_zeros((3,))
print(t_vector)
