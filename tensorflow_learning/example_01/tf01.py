import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#创建模拟输入输出的数据
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data *0.1 + 0.3

#构建线性回归模型
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases

#定义loss函数
loss = tf.reduce_mean(tf.square(y-y_data))
#定义优化器，使用梯度下降算法
optimizer = tf.train.GradientDescentOptimizer(0.5)
#定义训练模型
train = optimizer.minimize(loss)

#初始化全局变量
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for step in range(201):
    ##训练模型
    sess.run(train)
    if step % 20 == 0:
        #print(step, sess.run(Weights), sess.run(biases))
        print(sess.run(loss))

print("最终loss=%g" % (sess.run(loss)))



