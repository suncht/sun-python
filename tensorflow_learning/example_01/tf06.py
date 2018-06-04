import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#添加层
def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):
    layer_name = 'layer' + n_layer
    with tf.name_scope(layer_name):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
            tf.summary.histogram(layer_name + '/Weights', Weights) #可以在tensorboard中看到变化过程
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')
            tf.summary.histogram(layer_name + '/biases', biases)  #注意：tf.histogram_summary 变成 tf.summary.histogram
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b,)
        tf.summary.histogram(layer_name + '/outputs', outputs)
        return outputs

#模拟输入输出的测试数据集
x_data = np.linspace(-1, 1, 600)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

#定义输入输出的占位符
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_inputs')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_inputs')

#添加第一层
l1 = add_layer(xs, 1, 10, '1', activation_function=tf.nn.relu)
#添加输出层（第二层）
prediction = add_layer(l1, 10, 1, '2', activation_function=None)

#定义loss函数
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1], name='reduce_sum'), name='reduce_mean')
    tf.summary.scalar('loss', loss)  #注意：tf.train.scalar_summary 变成 tf.summary.scalar

#定义梯度下降优化算法
with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1, name='gradientDescentOptimizer').minimize(loss, name='minimize')

sess = tf.Session()
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter('C:/tf/logs/tf06', sess.graph) #注意:tf.train.summary 变成 tf.summary.FileWriter

sess.run(tf.global_variables_initializer())

feed_data = {xs: x_data, ys: y_data}
for i in range(1000):
    sess.run(train_step, feed_dict=feed_data)
    if i % 50 == 0:
        result = sess.run(merged, feed_dict=feed_data)
        writer.add_summary(result, i)  #每50次观察数值变化
    # prediction_value = sess.run(prediction, feed_dict=feed_data)
    # loss_value = sess.run(loss, feed_dict=feed_data)
    # for x in range(0, len(y_data)):
    #     print('%0.3f' % y_data[x][0], ' --- %0.3f' % prediction_value[x][0], ' --- %0.3f' % loss_value)
    # print('')


writer.close()
sess.close()

#不带单引号
#tensorboard --logdir=C:/tf/logs --debug
#http://127.0.0.1:6006/