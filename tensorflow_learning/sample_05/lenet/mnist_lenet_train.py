import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import time

#实现lenet5神经网络
mnist = input_data.read_data_sets('../../MNIST_DATA', one_hot=True)

# mnist_test_images = mnist.test.images[:200]
# mnist_test_labels = mnist.test.labels[:200]
# print(mnist_test_images.shape)
# print(mnist.train.images.shape)


# INPUT: [28x28x1]           weights: 0
# CONV5-32: [28x28x32]       weights: (5*5*1+1)*32
# POOL2: [14x14x32]          weights: 0
# CONV5-64: [14x14x64]       weights: (5*5*32+1)*64
# POOL2: [7x7x64]          weights: 0
# FC: [1x1x512]              weights: (7*7*64+1)*512
# FC: [1x1x10]              weights: (1*1*512+1)*10

#定义初始化权重
def weight_variable(shape, name):
    return tf.Variable(tf.truncated_normal(shape, stddev=0.1), name=name)

#定义初始化偏置
def biases_variable(shape, name):
    return tf.Variable(tf.constant(0.1, shape=shape), name=name)

#定义卷积核
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding='SAME')  #必须strides[0]=strides[3]=1

#定义池化层
def max_pooling_2x2(x):
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

#计算准确率
def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs, ys: v_ys, keep_prob: 1})
    corrent_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(corrent_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys, keep_prob: 1})
    return result

xs = tf.placeholder(tf.float32, [None, 784]) # 28*28
ys = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)

x_image = tf.reshape(xs, [-1, 28, 28, 1])

#第一层卷积层
w_conv1 = weight_variable([5,5,1,32], 'w_conv1')
b_conv1 = biases_variable([32], 'b_conv1')
h_conv1 = tf.nn.relu(conv2d(x_image, w_conv1) + b_conv1)
h_pool1 = max_pooling_2x2(h_conv1)

#第二层卷积层
w_conv2 = weight_variable([5,5,32,64], 'w_conv2')
b_conv2 = biases_variable([64], 'b_conv2')
h_conv2 = tf.nn.relu(conv2d(h_pool1, w_conv2) + b_conv2)
h_pool2 = max_pooling_2x2(h_conv2)

#卷积结果进行flat操作， 并且进入全连接神经网络进行预测
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])

#全连接网络1层
w_fc1 = weight_variable([7*7*64, 1024], 'w_fc1') #1024
b_fc1 = biases_variable([1024], 'w_fc1')
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, w_fc1) + b_fc1)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

#全连接网络2层
w_fc2 = weight_variable([1024, 10], 'w_fc2')
b_fc2 = biases_variable([10], 'b_fc2')
prediction = tf.nn.softmax(tf.matmul(h_fc1_drop, w_fc2) + b_fc2)

#损失函数
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1])) #loss函数为交叉熵
#cross_entropy2=tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits(logits, y_)) 包含了softmax和cross_entropy
train_step = tf.train.AdamOptimizer(0.0001).minimize(cross_entropy)
#train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

#评估
correct_prediction = tf.equal(tf.argmax(prediction,1), tf.argmax(ys,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

#测试
test_accuracy_sum = tf.Variable(0.0, name='test_accuracy_sum')
batch_accuracy = tf.placeholder(tf.float32)
new_test_accuracy_sum = tf.add(test_accuracy_sum, batch_accuracy)
update = tf.assign(test_accuracy_sum, new_test_accuracy_sum)

init_op = tf.global_variables_initializer()
saver_op = tf.train.Saver()

train_step_timer = time.time()
train_total_timer = time.time()
with tf.Session() as sess:
    sess.run(init_op)
    for i in range(1000):

        batch_xs, batch_ys = mnist.train.next_batch(100)  # 采用minbatch自助放回采样
        sess.run([train_step], feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 0.6})
        if i % 100 == 0:
            #print('第%d次训练结果：%g' % (i, compute_accuracy(batch_xs, batch_ys)))
            train_accuracy = sess.run(accuracy, feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 1})
            print('第%d次训练结果：%g' % (i, train_accuracy))
            print('耗时:%g' % (time.time() - train_step_timer))
            train_step_timer = time.time()

    save_path = saver_op.save(sess, './ckpts/mnist_lenet_result.ckpt')  # 将变量保存到文件中
    print('训练结果保存路径：%s' % save_path )
    print('总共耗时：%g' % (time.time() - train_total_timer))