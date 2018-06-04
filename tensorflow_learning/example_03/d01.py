import tensorflow as tf

sess = tf.InteractiveSession()

c1 = tf.constant(1)
v1 = tf.get_variable('v1', [1])

tf.global_variables_initializer().run()
# print(c1.eval())
# print(v1.eval())
#
# a1 = tf.constant(b'1.1', dtype=tf.string)
# a2 = tf.string_to_number(a1, out_type=tf.float32)
# print(a1.eval())
# print(a2.eval())
# print(tf.to_int32(a2).eval())
#
# a3 = tf.constant([1.2, 1.3, 1.4])
# print(tf.to_int32(a3).eval())
#
#
# a4 = tf.constant(['1.2', '1.3', '1.4'])
# print(tf.cast(a4, tf.float32).eval())

a5 = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
print(tf.shape(a5))