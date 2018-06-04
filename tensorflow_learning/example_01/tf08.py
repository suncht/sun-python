import tensorflow as tf
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

digits = load_digits()
X = digits.data
y = digits.target
# print(y)
# print('-----------')
y = LabelBinarizer().fit_transform(y)
# print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

def add_layer(inputs, in_size, out_size, layer_name, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)
    Wx_plus_b = tf.nn.dropout(Wx_plus_b, keep_prob=keep_prob)  #使用dropout防止过拟合
    if activation_function == None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b,)
    tf.summary.histogram(layer_name + '/outputs', outputs)
    return outputs

keep_prob = tf.placeholder(tf.float32)
xs = tf.placeholder(tf.float32, [None, 64])
ys = tf.placeholder(tf.float32, [None, 10])

l1 = add_layer(xs, 64, 100, 'l1', activation_function=tf.nn.tanh)
prediction = add_layer(l1, 100, 10, 'l2', activation_function=tf.nn.sigmoid)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))
tf.summary.scalar('loss', cross_entropy)
train_step = tf.train.GradientDescentOptimizer(0.6).minimize(cross_entropy)

sess = tf.Session()
merged = tf.summary.merge_all()

train_writer = tf.summary.FileWriter('c:/tf/logs/tf08/train', sess.graph)
test_writer = tf.summary.FileWriter('c:/tf/logs/tf08/test', sess.graph)

sess.run(tf.global_variables_initializer())
for i in range(1000):
    sess.run(train_step, feed_dict={xs:X_train, ys:y_train, keep_prob:0.5})
    if i % 50 == 0:
        train_result = sess.run(merged, feed_dict={xs:X_train, ys:y_train, keep_prob:1})
        test_result = sess.run(merged, feed_dict={xs:X_test, ys:y_test, keep_prob:1})
        train_writer.add_summary(train_result, i)
        test_writer.add_summary(test_result, i)
