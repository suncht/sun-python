import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_DATA/', one_hot=False)

images = np.asarray(mnist.test.images)

x_image = np.reshape(images, (images.shape[0], 28,28))
y_label = mnist.test.labels

for i in range(4*4):
    plt.subplot(4, 4, i + 1)
    title = "标签对应为："+ str(y_label[i])
    plt.title(title, fontproperties='SimHei')
    # plt.xlabel(' ')
    # plt.ylabel(' ')
    plt.imshow(x_image[i], cmap='gray')
plt.show()