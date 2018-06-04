import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

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

#模拟输入输出的测试数据集
x_data = np.linspace(-1, 1, 600)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise
#print(y_data)

#定义输入输出的占位符
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

#添加第一层
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
#添加输出层（第二层）
prediction = add_layer(l1, 10, 1, activation_function=None)

#定义loss函数
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
#定义梯度下降优化算法
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

##matplot绘制点
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.ion()  #避免plt卡死，可以实时看到效果
plt.show()

with tf.Session() as sess:
    sess.run(init)
    for i in range(1000):
        sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
        if i%50 == 0:
            #print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
            #print(sess.run(prediction,  feed_dict={xs: x_data, ys: y_data}))
            try:
                ax.lines.remove(lines[0])  #删除原来的线条
            except Exception:
                pass
            prediction_value = sess.run(prediction, feed_dict={xs: x_data, ys: y_data})
            lines = ax.plot(x_data, prediction_value, 'r-', linewidth=5) #绘制新的线条
            plt.pause(0.5)
