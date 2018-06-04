import os
import tensorflow as tf
import numpy as np
from PIL import Image

def read_cifar10(filename, batch_size, shuffle, one_hot):
    filename_queue = tf.train.string_input_producer([filename]) #生成一个queue队列
    reader = tf.TFRecordReader()
    _, serialized_example = reader.read(filename_queue) #返回文件名和文件
    features = tf.parse_single_example(serialized_example,
                                       features={
                                           'label': tf.FixedLenFeature([], tf.int64),
                                           'img_raw': tf.FixedLenFeature([], tf.string)
                                       }) #将image数据和label取出来
    image = tf.decode_raw(features['img_raw'], tf.uint8)
    image = tf.reshape(image, [32, 32, 3])
    #image = tf.cast(image, tf.float32) * (1.0 / 255) - 0.5
    #image = tf.image.per_image_standardization(image)
    label = tf.cast(features['label'], tf.int32)

    #return image, label;
    if shuffle:
        images, label_batch = tf.train.shuffle_batch(
            [image, label],
            batch_size=batch_size,
            num_threads=4,
            capacity=2000,
            min_after_dequeue=1500)
    else:
        images, label_batch = tf.train.batch(
            [image, label],
            batch_size=batch_size,
            num_threads=4,
            capacity=2000)

    if one_hot:
        label_batch = tf.one_hot(label_batch, depth=10)
    return images, label_batch

filename = 'cifar10_tfrecord/cifar10.train.tfrecords'
image, label = read_cifar10(filename=filename, batch_size=10, shuffle=True, one_hot=False)
with tf.Session() as sess: #开始一个会话
    tf.global_variables_initializer().run()
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    for i in range(10):
        example, l = sess.run([image, label])
        # print(example.shape)
        # print(l.shape)
        example = example[0]
        l = l[0]
        img = Image.fromarray(example, 'RGB')
        img.save(str(i) + '_Label_' + str(l) + '.jpg')  # 存下图片
    coord.request_stop()
    coord.join(threads)

