import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

def main():
    graph = tf.Graph()
    with graph.as_default():
        #input:定义输入节点
        with tf.name_scope('Input'):
            #计算图输入占位符
            X = tf.placeholder(tf.float32, [None, 784], name='X')
            Y = tf.placeholder(tf.float32, [None, 10], name='Y')
        #Inference:向前预测，创建一个线性模型：y = wx + b
        with tf.name_scope('Inference'):
            W = tf.Variable(tf.zeros([784, 10]), name='Weights')
            b = tf.Variable(tf.zeros([10]), name='Biases')
            logits = tf.add(tf.matmul(X, W), b)
            #softmax把logits变成预测概率分布
            with tf.name_scope('Softmax'):
                Y_pred = tf.nn.softmax(logits=logits)
        with tf.name_scope('Loss'):
            loss = tf.reduce_mean(tf.reduce_sum(-Y * tf.log(Y_pred), axis=1))
        #Train：定义预测节点
        with tf.name_scope('Train'):
            optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
            train_step = optimizer.minimize(loss=loss)
        #Evaluate:定义评估节点
        with tf.name_scope('Evaluate'):
            correct_prediction = tf.equal(tf.argmax(Y_pred, 1), tf.argmax(Y, 1))
            accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        #init:定义初始化节点
        init = tf.global_variables_initializer()

        writer = tf.summary.FileWriter(logdir='D:/tf/logs/sr', graph=tf.get_default_graph())
        writer.close()

        #加载数据集
        mnist = input_data.read_data_sets('../MNIST_DATA/', one_hot=True)

        sess = tf.InteractiveSession()
        sess.run(init)

        #批量训练
        for step in range(10000):
            batch_x, batch_y = mnist.train.next_batch(100)
            _, loss_r = sess.run([train_step, loss], feed_dict={X: batch_x, Y:batch_y})
            if step % 50 == 0:
                print('训练步骤：', step, '损失值：', loss_r)

        accuracy_score = sess.run(accuracy, feed_dict={X: mnist.test.images, Y: mnist.test.labels})
        print('测试准确率：', accuracy_score)

        sess.close()

if __name__ == '__main__':
    main()