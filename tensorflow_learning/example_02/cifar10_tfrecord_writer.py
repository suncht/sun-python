import os
import tensorflow as tf
from PIL import Image

cwd = 'cifar10_images/train/'
writer = tf.python_io.TFRecordWriter('cifar10_tfrecord/cifar10.train.tfrecords') #要生成的文件
for path in os.listdir(cwd):
    index = int(path) #类别
    real_path = os.path.join(cwd, path)
    print('-----处理目录:'+real_path )
    for img_name in os.listdir(real_path):
        img_path = os.path.join(real_path, img_name) #每一个图片的地址
        img = Image.open(img_path)
        img = img.resize((32, 32))
        img_raw = img.tobytes() #将图片转化为二进制格式
        example = tf.train.Example(features=tf.train.Features(feature={
            'label': tf.train.Feature(int64_list=tf.train.Int64List(value=[index])),
            'img_raw': tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw]))
        })) #example对象对label和image数据进行封装
        writer.write(example.SerializeToString()) #序列化为字符串
        print('图片【' + img_name + '】写入TFRecord')
writer.close()