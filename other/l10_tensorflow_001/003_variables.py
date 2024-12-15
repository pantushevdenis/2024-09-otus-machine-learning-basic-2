import tensorflow as tf
print(tf.__version__)

tensor_weights = tf.random.normal([3, 2], mean=0.0, stddev=0.4)
print(tensor_weights)
w = tf.Variable(tensor_weights, name ='weights')
print(w)
tensor_biases = tf.zeros([2])
print(tensor_biases)
b = tf.Variable(tensor_biases, name ='biases')
print(b)
