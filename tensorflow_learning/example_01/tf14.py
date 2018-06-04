import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

mnist = input_data.read_data_sets('MNIST_DATA/', one_hot=True)

#添加层
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

xs = tf.placeholder(tf.float32, [None, 784]) # 28*28

encoder = add_layer(xs, 784, 14*14, activation_function=tf.nn.sigmoid)
decoder = add_layer(encoder, 14*14, 784, activation_function=tf.nn.sigmoid)
loss = tf.reduce_mean(tf.pow(xs - decoder, 2))
train_step = tf.train.RMSPropOptimizer(0.05).minimize(loss)

total_batch = int(mnist.train.num_examples / 256)
with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    for epoch in range(20):
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(100)  # 采用minbatch自助放回采样
            _, loss_r = session.run([train_step, loss], feed_dict={xs: batch_xs})
            if i % 50 ==0 :
                print(loss_r)
    encode_decode = session.run(decoder, feed_dict={xs: mnist.test.images})

print(encode_decode.shape)

images = np.reshape(encode_decode, (encode_decode.shape[0], 28,28))

for i in range(4*4):
    plt.subplot(4, 4, i + 1)
    plt.imshow(images[i], cmap='gray')
plt.show()
