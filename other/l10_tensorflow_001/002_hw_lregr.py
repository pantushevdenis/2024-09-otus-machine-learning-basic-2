import numpy as np
import tensorflow as tf

N_SAMPLES = 1000
BATCH_SIZE = 100
NUM_STEP = 20000

# Исходные данные для обучения, stub
x_data = np.random.uniform(1, 10, (N_SAMPLES, 1))
#print(x_data)
y_data = 2 * x_data + 1 + np.random.normal(0, 2, (N_SAMPLES, 1))
# print(y_data)

#

# x = tf.placeholder(tf.float32, shape=(BATCH_SIZE, 1))
# y = tf.placeholder(tf.float32, shape=(BATCH_SIZE, 1))

# t_k = np.random.normal((1, ))


initializers_zeros = tf.keras.initializers.Zeros()
initializers_random_normal = tf.keras.initializers.RandomNormal()

t_k = initializers_random_normal((1, 1))
print(t_k)
t_b = initializers_zeros((1,))
print(t_b)



# with tf.variable_scope('linear_regression'):
#     k = tf.Variable(t_k, name='slope')
#     b = tf.Variable(t_b, name='bias')
#
# y_pred = tf.linalg.matmul(x, k) + b
# loss = tf.math.reduce_sum((y - y_pred) ** 2)
#
# optimizer = tf.train .GradientDescendentOptimizer().minimize(loss)
#
# display_step = 100
# with tf.Session() as sess:
#     sess.run(tf.initialize_global_variables())
