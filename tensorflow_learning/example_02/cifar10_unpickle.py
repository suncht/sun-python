import numpy as np
import os
from scipy import misc

# 解压缩，返回解压后的字典
def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

#创建目录
def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

# 生成训练集图片，如果需要png格式，只需要改图片后缀名即可。
for j in range(1, 6):
    dataName = "cifar10_data/data_batch_" + str(j)  # 读取当前目录下的data_batch12345文件，dataName其实也是data_batch文件的路径，本文和脚本文件在同一目录下。
    data = unpickle(dataName)
    print(dataName + " is loading...")

    for i in range(0, 10000):
        img = np.reshape(data[b'data'][i], (3, 32, 32))
        img = img.transpose(1, 2, 0)  # 读取image
        mkdir('cifar10_images/train/' + str(data[b'labels'][i]) + '/')
        picName = 'cifar10_images/train/' + str(data[b'labels'][i]) + '/' + str(i + (j - 1) * 10000) + '.jpg'  # Xtr['labels']为图片的标签，值范围0-9，本文中，train文件夹需要存在，并与脚本文件在同一目录下。
        misc.imsave(picName, img)
    print(dataName + " loaded.")

print("test_batch is loading...")

# 生成测试集图片
data = unpickle("cifar10_data/test_batch")
for i in range(0, 10000):
    img = np.reshape(data[b'data'][i], (3, 32, 32))
    img = img.transpose(1, 2, 0)
    mkdir('cifar10_images/test/' + str(data[b'labels'][i]) + '/')
    picName = 'cifar10_images/test/' + str(data[b'labels'][i]) + '/' + str(i) + '.jpg'
    misc.imsave(picName, img)
print("cifar10 image loaded.")