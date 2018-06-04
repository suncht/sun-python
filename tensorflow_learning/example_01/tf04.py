import tensorflow as tf

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run(output, feed_dict={input1:[1.0], input2:[2.0]}))


input11 = tf.placeholder(tf.float32, [2,2])
input21 = tf.placeholder(tf.float32, [2,2])

output1 = tf.matmul(input11, input21)

with tf.Session() as sess:
    print(sess.run(output1, feed_dict={input11:[[1.0, 2.0],[1.4,5.0]], input21:[[2.0, 3.0],[1.4,5.0]]}))