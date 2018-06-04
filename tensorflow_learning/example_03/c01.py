import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

image1 = np.reshape(np.linspace(0, 255, 32*32, dtype=np.float32), (32,32, 1))
image2 = np.reshape(np.linspace(0, 255, 32*32, dtype=np.float32), (32,32, 1))


with tf.Graph().as_default():
    sess = tf.Session()

    def conv_relu(input, kernal_shape, bias_shape):
        weigths = tf.get_variable(name='weights', shape = kernal_shape, initializer=tf.random_normal_initializer())
        biases = tf.get_variable(name='biases', shape=bias_shape, initializer=tf.constant_initializer(0.0))
        conv = tf.nn.conv2d(input=input, filter=weigths, strides=[1,1,1,1], padding='SAME')

        return tf.nn.relu(conv + biases)

    def my_image_filter(input_images):
        x_image = tf.reshape(input_images, [-1, 32, 32, 1])
        with tf.variable_scope('conv1'):
            relu1 = conv_relu(x_image, [5,5,1,32], [32])
        with tf.variable_scope('conv2'):
            relu2 = conv_relu(relu1, [5,5,32,32], [32])


    sess.run(tf.global_variables_initializer())

    with tf.variable_scope("image_filters") as scope:
        result1 = my_image_filter(image1)
        scope.reuse_variables()
        result2 = my_image_filter(image2)

    sess.run(result1.name)


