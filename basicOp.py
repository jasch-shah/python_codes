'''
Basic Operations example using TensorFlow library.
'''
from __future__ import print_function

import tensorflow as tf

#basic constant op
#value returned by constructor
#of constant op
a = tf.constant(2)
b = tf.constant(3)

with tf.Session() as sess:
	print("a=2,b=3")
	print("Addition with constant: %i"%sess.run(a+b))
	print("Multiplication with constant: %i"%sess.run(a*b))

	# Basic Operations with variable as graph input
# The value returned by the constructor represents the output
# of the Variable op. (define as input when running session)
# tf Graph input

a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

add = tf.add(a,b)
mul = tf.multiply(a,b)

with tf.Session() as sess:
print("Addition with variables: %i"%sess.run(add,feed_dict={a:2,b:3}))	
print("Multiplication with variables: %i"%sess.run(mul,feed_dict={a:2,b:3}))
# ----------------
# More in details:
# Matrix Multiplication from TensorFlow official tutorial

# Create a Constant op that produces a 1x2 matrix.  The op is
# added as a node to the default graph.
#
# The value returned by the constructor represents the output
# of the Constant op.


