import os
import numpy as np
import cv2
import re

IMAGE_SIZE =120

# 读取训练数据
images = []
labels = []

# 按照指定图像大小调整尺寸
def resize_image(image, height=IMAGE_SIZE, width=IMAGE_SIZE):

    return cv2.resize(image, (height, width))


def read_path(path_name):
    for dir_item in os.listdir(path_name):
        # 从初始路径开始叠加，合并成可识别的操作路径
        full_path = os.path.abspath(os.path.join(path_name, dir_item))
        if os.path.isdir(full_path):  # 如果是文件夹，继续递归调用
            read_path(full_path)
        else:  # 文件
            if dir_item.endswith('.jpg'):
                #image = cv2.imread(full_path, cv2.IMREAD_GRAYSCALE) # 将RGB图片转为灰度
                image = cv2.imread(full_path)
                image = resize_image(image, IMAGE_SIZE, IMAGE_SIZE)
                #cv2.imwrite('1.jpg', image)

                images.append(image)
                path_name1 = re.sub('\D','',path_name)
                labels.append(str(path_name1))

        #print(images,labels)

    return images, labels


# 从指定路径读取训练数据
def load_dataset(path_name):
    images, labels = read_path(path_name)

    # 将输入的所有图片转成四维数组，尺寸为(图片数量*IMAGE_SIZE*IMAGE_SIZE*3)
    # 一个像素3个颜色值(RGB)
    images = np.array(images)
    print(images.shape)

    # 标注数据
    labels = np.array(labels)
    print(labels.shape)
    return images, labels



if __name__ == '__main__':

    images, labels = load_dataset('G:/code/study/source_code/LFW/select_WebFace')

