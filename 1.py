import tensorflow as tf
import numpy as np

tf.set_random_seed(1234)
a = tf.random_uniform([1])
b = tf.random_normal([1])
with tf.Session() as sess1:
    print(sess1.run(a))  # generates 'A1'
    print(sess1.run(a)) # generates 'A2'
    print(sess1.run(b)) # generates 'B1'
    print(sess1.run(b))  # generates 'B2'
with tf.Session() as sess2:
    print(sess2.run(a))  # generates 'A1'
    print(sess2.run(a)) # generates 'A2'
    print(sess2.run(b)) # generates 'B1'
    print(sess2.run(b))  # generates 'B2'