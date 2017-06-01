import tensorflow as tf
import numpy as np

# tf.set_random_seed(1234)
# a = tf.random_uniform([1])
# b = tf.random_uniform([1])
# with tf.Session() as sess1:
#     print(sess1.run(a))  # generates 'A1'
#     print(sess1.run(a)) # generates 'A2'
#     print(sess1.run(b)) # generates 'B1'
#     print(sess1.run(b))  # generates 'B2'
# with tf.Session() as sess2:
#     print(sess2.run(a))  # generates 'A1'
#     print(sess2.run(a)) # generates 'A2'
#     print(sess2.run(b)) # generates 'B1'
#     print(sess2.run(b))  # generates 'B2'

# all = dict()
# all[1] =2
# print(all)

saver = tf.train.Saver

a = tf.Variable([1,2])
b = tf.Variable([2,4])
c = tf.matmul(a,b,transpose_b=True)
tf.add_to_collection('c',c)
sess = tf.Session()
sess.run(c)
saver.save(sess,'my_model')