import tensorflow as tf

sess = tf.InteractiveSession()

with tf.name_scope('scop1') as scope0:
    #print(scope0.name)
    with tf.variable_scope('foo2') as scope:
        print(scope.name)
        with tf.name_scope('scop2') as scope1:
            #print(scope1.name)
            v1 = tf.get_variable(name='v1', shape=[2,2], dtype=tf.float32, initializer=tf.constant_initializer(1.0))
            v3 = tf.get_variable(name='v3', shape=[2,2], dtype=tf.float32, initializer=tf.constant_initializer(3.0))
            scope.reuse_variables()
            v2 = tf.get_variable(name='v1')

    with tf.variable_scope("foo2", reuse=True):
        v4 = tf.get_variable(name='v3')
        v5 = tf.get_variable(name='v1')

    v6 = tf.get_variable('aa', [1])

with tf.variable_scope('a') as a:
    with tf.variable_scope('b') as b:
        with tf.variable_scope(b) as c:
            print('---->' + a.name) # a
            print('---->' + b.name) # a/b
            print('---->' + c.name) # a/b
            v6 = tf.get_variable('v6', [1])
            print('---->' + v6.name) # a/b/v6:0



print(v1.name)
print(v2.name)
print(v3.name)
print(v4.name)
print(v5.name)
print(v6.name)


with tf.variable_scope("foo", initializer=tf.constant_initializer(0.4)):
    v1 = tf.get_variable("v", [1])

    w2 = tf.get_variable("w", [1], initializer=tf.constant_initializer(0.3));

    with tf.variable_scope("bar"):
        v3 = tf.get_variable("v", [1])

    with tf.variable_scope("baz", initializer=tf.constant_initializer(0.2)):
        v4 = tf.get_variable("v", [1])


tf.global_variables_initializer().run()
print(v1.eval())  # Default initializer as set above.
print(w2.eval())  # Specific initializer overrides the default.
print(v3.eval())  # Inherited default initializer.
print(v4.eval())  # Changed default initializer.
sess.close()