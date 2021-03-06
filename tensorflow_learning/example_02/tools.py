import numpy as np
import tensorflow as tf

def conv(layer_name, x, out_channels, kernel_size=[3,3], stride=[1,1,1,1], is_pretrain=True):
    '''
    定义卷积层
    :param layer_name: 卷积层名称
    :param x: 输入
    :param out_channels: 输出通道
    :param kernel_size: 卷积核大小
    :param stride: 步长
    :param is_pretrain:
    :return:
    '''
    in_channels = x.get_shape()[-1]
    with tf.variable_scope(layer_name):
        w = tf.get_variable(name='weights',
                            trainable=is_pretrain,
                            shape=[kernel_size[0], kernel_size[1], in_channels, out_channels],
                            initializer=tf.contrib.layers.xavier_initializer())
        b = tf.get_variable(name='biases',
                            trainable=is_pretrain,
                            shape=[out_channels],
                            initializer=tf.constant_initializer(0.0))
        x = tf.nn.conv2d(x, w, strides=stride, padding='SAME', name='conv')
        x = tf.nn.bias_add(x, b, name='bias_add')
        x = tf.nn.relu(x, name='relu')
        return x

def pool(layer_name, x, kernel=[1,2,2,1], stride=[1,2,2,1], is_max_pool=True):
    '''
    池化层
    :param layer_name: 名称
    :param x: 输入
    :param kernel: 卷积核大小
    :param stride: 步长
    :param is_max_pool: 最大值
    :return:
    '''
    if is_max_pool:
        x = tf.nn.max_pool(x, kernel, strides=stride, padding='SAME', name=layer_name)
    else:
        x = tf.nn.avg_pool(x, kernel, strides=stride, padding='SAME', name=layer_name)
    return x

def batch_norm(x):
    '''
    批量正则化
    :param x:
    :return:
    '''
    epsilon = 1e-3
    batch_mean, batch_var = tf.nn.moments(x, [0])
    x = tf.nn.batch_normalization(x, mean=batch_mean, variance=batch_var, offset=None, scale=None, variance_epsilon=epsilon)
    return x

def FC_layer(layer_name, x, out_nodes, activaction_function=None):
    '''
    全连接神经网络
    :param layer_name:
    :param x:
    :param out_nodes:
    :return:
    '''
    shape = x.get_shape()
    if len(shape) == 4:
        size = shape[1].value * shape[2].value * shape[3].value
    else:
        size = shape[-1].value

    with tf.variable_scope(layer_name):
        w = tf.get_variable('weights',
                            shape=[size, out_nodes],
                            initializer=tf.contrib.layers.xavier_initializer())
        b = tf.get_variable('biases',
                            shape=[out_nodes],
                            initializer=tf.constant_initializer(0.0))
        flat_x = tf.reshape(x, [-1, size])  # flatten into 1D

        x = tf.nn.bias_add(tf.matmul(flat_x, w), b)
        # x = tf.nn.relu(x)
        if activaction_function == None:
            return x
        else:
            return activaction_function(x)

def loss(logits, labels):
    '''
    损失函数
    :param logits:
    :param labels:
    :return:
    '''
    with tf.name_scope('loss') as scope:
        cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=labels, name='cross-entropy')
        loss = tf.reduce_mean(cross_entropy, name='loss')
        tf.summary.scalar(scope + '/loss', loss)

    return loss

def accuracy(logits, labels):
    '''
    评估准确率
    :param logits:
    :param labels:
    :return:
    '''
    with tf.name_scope('accuracy') as scope:
        correct = tf.equal(tf.arg_max(logits, 1), tf.arg_max(labels, 1))
        correct = tf.cast(correct, tf.float32)
        accuracy = tf.reduce_mean(correct) * 100.0
        tf.summary.scalar(scope + '/accuracy', accuracy)
    return accuracy

def num_correct_prediction(logits, labels):
    correct =  tf.equal(tf.argmax(logits, 1), tf.argmax(labels, 1))
    correct = tf.cast(correct, tf.int32)
    n_correct = tf.reduce_sum(correct)
    return n_correct

def optimize(loss, learning_rate, global_step):
    '''
    优化器，默认使用梯度下降优化器
    :param loss:
    :param learning_rate:
    :param global_step:
    :return:
    '''
    with tf.name_scope('optimize') as scope:
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
        train_op = optimizer.minimize(loss, global_step=global_step)
    return train_op

def load(data_path, session):
    data_dict = np.load(data_path, encoding='latin1').item()

    keys = sorted(data_dict.keys())
    for key in keys:
        with tf.variable_scope(key, reuse=True):
            for subkey, data in zip(('weights', 'biases'), data_dict[key]):
                session.run(tf.get_variable(subkey).assign(data))


def test_load():
    data_path = './/vgg16_pretrain//vgg16.npy'

    data_dict = np.load(data_path, encoding='latin1').item()
    keys = sorted(data_dict.keys())
    for key in keys:
        weights = data_dict[key][0]
        biases = data_dict[key][1]
        print('\n')
        print(key)
        print('weights shape: ', weights.shape)
        print('biases shape: ', biases.shape)

def load_with_skip(data_path, session, skip_layer):
    '''
    加载数据时，可以跳过加载某些层
    :param data_path:
    :param session:
    :param skip_layer:
    :return:
    '''
    data_dict = np.load(data_path, encoding='latin1').item()
    for key in data_dict:
        if key not in skip_layer:
            with tf.variable_scope(key, reuse=True):
                for subkey, data in zip(('weights', 'biases'), data_dict[key]):
                    session.run(tf.get_variable(subkey).assign(data))

def print_all_variables(train_only=True):
    """
    打印所有参数
    """
    if train_only:
        t_vars = tf.trainable_variables()
        print("  [*] printing trainable variables")
    else:
        try: # TF1.0
            t_vars = tf.global_variables()
        except: # TF0.12
            t_vars = tf.all_variables()
        print("  [*] printing global variables")
    for idx, v in enumerate(t_vars):
        print("  var {:3}: {:15}   {}".format(idx, str(v.get_shape()), v.name))


def weight(kernel_shape, is_uniform=True):
    '''
    权重初始化
    '''
    w = tf.get_variable(name='weights',
                        shape=kernel_shape,
                        initializer=tf.contrib.layers.xavier_initializer())
    return w

#%%
def bias(bias_shape):
    '''
    偏置初始化
    '''
    b = tf.get_variable(name='biases',
                        shape=bias_shape,
                        initializer=tf.constant_initializer(0.0))
    return b