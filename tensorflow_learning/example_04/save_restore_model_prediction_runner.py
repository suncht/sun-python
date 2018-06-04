from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("../MNIST_DATA/", one_hot=True)

import tensorflow as tf
import numpy as np
import random

# Parameters
model_path = "temp/model.ckpt"

# Network Parameters
n_hidden_1 = 256 # 1st layer number of features
n_hidden_2 = 256 # 2nd layer number of features
n_input = 784 # MNIST data input (img shape: 28*28)
n_classes = 10 # MNIST total classes (0-9 digits)

# tf Graph input
x = tf.placeholder("float", [None, n_input])

# Create model
def multilayer_perceptron(x, weights, biases):
    # Hidden layer with RELU activation
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    # Hidden layer with RELU activation
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)
    # Output layer with linear activation
    out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
    return out_layer

# Store layers weight & bias
weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}

# Construct model
pred = multilayer_perceptron(x, weights, biases)


# Initializing the variables
#init = tf.global_variables_initializer()
# 'Saver' op to save and restore all the variables
saver = tf.train.Saver()
# Running a new session
print("Starting Test...")
with tf.Session() as sess:
    # Initialize variables
    #sess.run(init)

    # Restore model weights from previously saved model
    saver.restore(sess, model_path)
    print("Model restored from file: %s" % model_path)

    couint = len(mnist.test.labels)
    index = random.randint(0,couint)

    print(mnist.test.images.shape)
    print(mnist.test.images[index:index+1].shape)
    #data = zip(mnist.test.images[index], mnist.test.labels[index])
    to_test = mnist.test.images[index:index+1]
    pred_value = tf.argmax(pred, 1)
    print("预测值:", pred_value.eval( {x: to_test}))
    print("真实值：", mnist.test.labels[index:index+1])
