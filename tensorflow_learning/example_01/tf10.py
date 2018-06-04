import tensorflow as tf
import numpy as np
# W = tf.Variable([[1,2,3], [3,4,5]], dtype=tf.float32, name='weights')
# b = tf.Variable([[1,2,3]], dtype=tf.float32, name='biases')
#
# init = tf.global_variables_initializer()
#
# saver = tf.train.Saver()
#
# with tf.Session() as sess:
#     sess.run(init)
#     save_path = saver.save(sess, 'my_net/save_net.ckpt') #将变量保存到文件中
#     print('保存路径：' +save_path)

W = tf.Variable(np.arange(6).reshape((2,3)), dtype=tf.float32, name='weights')
b = tf.Variable(np.arange(3).reshape((1,3)), dtype=tf.float32, name='biases')

saver = tf.train.Saver()
with tf.Session() as sess:
    saver.restore(sess, 'my_net/save_net.ckpt') #从文件中读取变量
    print(sess.run(W))
    print(sess.run(b))