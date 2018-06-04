import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import datetime

mnist = input_data.read_data_sets("../MNIST_DATA/", one_hot=True)

def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs, ys: batch_ys, keep_prob: 1})
    corrent_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(corrent_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys, keep_prob: 1})
    return result

#定义初始化权重
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

#定义初始化偏置
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

#定义卷积核
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding='SAME')  #必须strides[0]=strides[3]=1

#定义池化层
def max_pooling_2x2(x):
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

with tf.Graph().as_default():
    xs = tf.placeholder(tf.float32, [None, 784]) # 28*28
    ys = tf.placeholder(tf.float32, [None, 10])
    keep_prob = tf.placeholder(tf.float32)

    x_image = tf.reshape(xs, [-1, 28, 28, 1])

    #卷积网络1层
    W_conv1 = weight_variable([5,5,1,32])  #patch:5*5  insize:1 outsize:32
    b_conv1 = bias_variable([32])
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)    #output size: 28*28*32
    h_pool1 = max_pooling_2x2(h_conv1)                          #output_size: 14*14*32

    #卷积网络2层
    W_conv2 = weight_variable([5,5,32,64])  #patch:5*5  insize:32 outsize:64
    b_conv2 = bias_variable([64])
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)    #output size: 14*14*64
    h_pool2 = max_pooling_2x2(h_conv2)                          #output_size: 7*7*64

    #卷积结果进行flat操作， 并且进入全连接神经网络进行预测
    h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])

    #全连接网络1层
    W_fc1 = weight_variable([7*7*64, 1024]) #1024
    b_fc1 = bias_variable([1024])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    #全连接网络2层
    W_fc2 = weight_variable([1024, 10])
    b_fc2 = bias_variable([10])
    prediction = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

    #cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1])) #loss函数为交叉熵
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=ys, logits=prediction))
    tf.scalar_summary(cross_entropy.op.name, cross_entropy)
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    summary = tf.merge_all_summaries()
    summary_writer = tf.train.SummaryWriter('log/tf09', sess.graph)

    begin = datetime.datetime.now()
    for i in range(20000):
        begin_per = datetime.datetime.now()
        batch_xs, batch_ys = mnist.train.next_batch(50)  #采用minbatch自助放回采样
        sess.run([train_step], feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 0.5})
        if i % 100 == 0:
            print(compute_accuracy(batch_xs, batch_ys))
            print('第'+str(i)+'次耗时：', str((datetime.datetime.now() - begin_per)))
            summary_str = sess.run(summary, feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 0.5})
            summary_writer.add_summary(summary_str, i)

    print(compute_accuracy(mnist.test.images, mnist.test.labels))
    print("卷积神经网络总耗时：", str((datetime.datetime.now() - begin)))
    sess.close()


#结果是： 0.9224（减小数据量， 全连接网络隐含层为200）
#结果时：0.952
#第490次耗时： 0:00:14.344000
#卷积神经网络总耗时： 0:14:55.004997

#迭代20000， 结果为0.9907  总耗时： 1:05:44.110557