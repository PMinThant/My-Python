# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 21:18:01 2019

@author: User
"""

import tensorflow as tf
x = tf.placeholder(tf.string)

with tf.Session() as sess:
    output = sess.run(x, feed_dict={x: 'Hello World'})