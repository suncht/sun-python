import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_DATA', one_hot=True)

#定义超参数
lr = 0.001  #学习率
train_iters = 100000 #迭代次数
batch_size = 128 #自助放回采样个数

n_inputs = 28   #图片大小:28*28，一行28列
n_steps = 28    #图片有28行
n_hidden_unis = 128 #隐藏层神经元个数
n_classes = 10  #分类个数

x = tf.placeholder(tf.float32, [None, n_steps, n_inputs])
y = tf.placeholder(tf.float32, [None, 10])

weights = {
    #(28, 128)
    'in': tf.Variable(tf.random_normal([n_inputs, n_hidden_unis])),
    #(128, 10)
    'out': tf.Variable(tf.random_normal([n_hidden_unis, n_classes]))
}

biases = {
    'in': tf.Variable(tf.constant(0.1, shape=[n_hidden_unis,])),
    'out': tf.Variable(tf.constant(0.1, shape=[n_classes,]))
}

def RNN(X, weights, biases):
    pass

pred = RNN(x, weights, biases)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred, y))
train_op = tf.train.AdamOptimizer(lr).minimize(cost)

correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    step = 0
    while step * batch_size < train_iters:
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        batch_xs = batch_xs.reshape([batch_size, n_steps, n_inputs])
        sess.run([train_op], feed_dict={x: batch_xs, y:batch_ys})
        if step % 20 ==0:
            sess.run(accuracy, feed_dict={x: batch_xs, y: batch_ys})
        step += 1

