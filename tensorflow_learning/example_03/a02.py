import tensorflow as tf

v1 = tf.Variable(tf.random_normal([4, 4], stddev=0.5), name='v1')
v2 = tf.Variable(tf.random_normal([4], stddev=0.1), name='v2')

#saver = tf.train.Saver() #可以不需要初始化， 因为所有变量都会restore
saver = tf.train.Saver({'v1': v1})  #只是部分变量初始化， 所以其他两个还需要初始化

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op) #还需要初始化， 因为v2需要初始化
    saver.restore(sess, 'tmp/model.ckpt')

    print(sess.run(v1))
    print(sess.run(v2))

    print(sess.run(tf.shape(v1)))