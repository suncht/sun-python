import tensorflow as tf

v1 = tf.Variable(tf.random_normal([4, 4], stddev=0.5), name='v1')
v2 = tf.Variable(tf.random_normal([4], stddev=0.1), name='v2')

saver = tf.train.Saver({'v1': v1})

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    print(sess.run(v1))
    print(sess.run(v2))
    save_path = saver.save(sess, 'tmp/model.ckpt')
    print(save_path)
