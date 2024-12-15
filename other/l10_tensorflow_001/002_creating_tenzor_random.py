import tensorflow as tf
import tensorflow.keras. initializers as inits

inits_random_uniform_0_to_10 = inits.RandomUniform(minval=0, maxval=10)

vect_rand = inits_random_uniform_0_to_10((3,))
print(vect_rand)

inits_random_normal_05_02 = inits.RandomNormal(mean=0.5, stddev=0.2)
matrix_rand = inits_random_normal_05_02((3, 3))
print(matrix_rand)
