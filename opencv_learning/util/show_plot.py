from matplotlib import pyplot as plt
from pylab import mpl

def set_ch():
	mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
	mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
set_ch()

def showPlot(images, titles, col=2):
    length = int(len(images))
    row = int((length + 1) / col)
    for i in range(length):
        plt.subplot(row, col, i + 1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i], )
        plt.xticks([])
        plt.yticks([])
    plt.show()