import tools
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('../MNIST_DATA/', one_hot=True)

is_pretrain = False
learning_rate = 0.5
MAX_STEP = 5000
train_log_dir = './/logs//train//'
val_log_dir = './/logs//val//'

with tf.Graph().as_default():
    with tf.name_scope('inputs'):
        x = tf.placeholder(tf.float32, shape=[None, 784])
        y_ = tf.placeholder(tf.float32, shape=[None, 10])
        x_images = tf.reshape(x, [-1, 28, 28, 1])

    with tf.name_scope('conv_net'):
        outputs = tools.conv('conv1_1', x_images, 32, kernel_size=[3, 3], stride=[1, 1, 1, 1], is_pretrain=is_pretrain)
        #outputs = tools.conv('conv1_2', outputs, 32, kernel_size=[3, 3], stride=[1, 1, 1, 1], is_pretrain=is_pretrain)
        outputs = tools.pool('pool1', outputs, kernel=[1, 2, 2, 1], stride=[1, 2, 2, 1], is_max_pool=True)

        outputs = tools.conv('conv2_1', outputs, 64, kernel_size=[3, 3], stride=[1, 1, 1, 1], is_pretrain=is_pretrain)
        #outputs = tools.conv('conv2_2', outputs, 64, kernel_size=[3, 3], stride=[1, 1, 1, 1], is_pretrain=is_pretrain)
        outputs = tools.pool('pool2', outputs, kernel=[1, 2, 2, 1], stride=[1, 2, 2, 1], is_max_pool=True)

        outputs = tools.FC_layer('fc6', outputs, out_nodes=1024, activaction_function=tf.nn.relu)
        outputs = tools.batch_norm(outputs)
        outputs = tools.FC_layer('fc7', outputs, out_nodes=1024, activaction_function=tf.nn.relu)
        outputs = tools.batch_norm(outputs)
        logits = tools.FC_layer('fc8', outputs, out_nodes=10, activaction_function=tf.nn.softmax)

    loss = tools.loss(logits, y_)
    accuracy = tools.accuracy(logits, y_)
    my_global_step = tf.Variable(0, name='global_step', trainable=False)
    train_op = tools.optimize(loss, learning_rate, my_global_step)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    summary_op = tf.summary.merge_all()
    tra_summary_writer = tf.summary.FileWriter(train_log_dir, sess.graph)

    for step in range(MAX_STEP):
        batch_xs, batch_ys = mnist.train.next_batch(100)  #采用minbatch自助放回采样
        _train_r, _train_acc, _train_loss = sess.run([train_op, accuracy, loss], feed_dict={x: batch_xs, y_: batch_ys})
        if step % 50 == 0 or (step + 1) == MAX_STEP:
            print('步骤'+str(step) + '结果：', _train_acc, ' 损失值：',_train_loss)
            summary_str = sess.run(summary_op, feed_dict={x: batch_xs, y_: batch_ys})
            tra_summary_writer.add_summary(summary_str, step)
        if step % 500 == 0 or (step + 1) == MAX_STEP:
            valid_batch_xs, valid_batch_ys = mnist.validation.next_batch(100)
            valid_train_acc = sess.run(accuracy, feed_dict={x: batch_xs, y_: batch_ys})
            print('交叉验证结果：', valid_train_acc)
            summary_str = sess.run(summary_op, feed_dict={x: valid_batch_xs, y_: valid_batch_ys})
            tra_summary_writer.add_summary(summary_str, step)


    a = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
    print("测试集准确率：",a)
