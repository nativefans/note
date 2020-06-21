
import random

import numpy as np
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D , AveragePooling2D
from keras.optimizers import SGD
from keras.utils import np_utils
from keras.models import load_model
from keras import backend as K
import matplotlib.pyplot as plt


from load_face_dataset import load_dataset, IMAGE_SIZE

MODEL_PATH = 'G:\\code\\study\\source_code\\LFW\\select_WebFace\\face_train_model_True2.h5'
class Dataset:
    def __init__(self, path_name):
        # 训练集
        self.train_images = None
        self.train_labels = None

        # 验证集
        self.valid_images = None
        self.valid_labels = None

        # 测试集
        self.test_images = None
        self.test_labels = None

        # 数据集加载路径
        self.path_name = path_name

        # 当前库采用的维度顺序
        self.input_shape = None

    # 加载数据集并按照交叉验证的原则划分数据集并进行相关预处理工作
    def load(self, img_rows=IMAGE_SIZE, img_cols=IMAGE_SIZE,
             img_channels=3):
        # 加载数据集到内存
        images, labels = load_dataset(self.path_name)

        train_images, valid_images, train_labels, valid_labels = \
            train_test_split(images, labels, test_size=0.1,random_state=random.randint(0, 100))
        #print(train_labels)
        valid_images, test_images, valid_labels, test_labels = \
            train_test_split(valid_images, valid_labels, test_size=0.5,random_state=random.randint(0, 100))

        # 当前的维度顺序如果为'th'，则输入图片数据时的顺序为：channels,rows,cols，否则:rows,cols,channels
        # 这部分代码就是根据keras库要求的维度顺序重组训练数据集
        if K.image_dim_ordering() == 'th':
            train_images = train_images.reshape(train_images.shape[0], img_channels, img_rows, img_cols)
            valid_images = valid_images.reshape(valid_images.shape[0], img_channels, img_rows, img_cols)
            test_images = test_images.reshape(test_images.shape[0], img_channels, img_rows, img_cols)
            self.input_shape = (img_channels, img_rows, img_cols)
        else:
            train_images = train_images.reshape(train_images.shape[0], img_rows, img_cols, img_channels)
            valid_images = valid_images.reshape(valid_images.shape[0], img_rows, img_cols, img_channels)
            test_images = test_images.reshape(test_images.shape[0], img_rows, img_cols, img_channels)
            self.input_shape = (img_rows, img_cols, img_channels)

            # 输出训练集、验证集、测试集的数量
            print(train_images.shape[0], 'train samples')
            print(valid_images.shape[0], 'valid samples')
            print(test_images.shape[0], 'test samples')

            # 我们的模型使用categorical_crossentropy（交叉熵损失函数）作为损失函数，
            # 该函数要求标签集必须采用独热编码的形式，
            # 因此需要根据类别数量nb_classes将
            # 类别标签进行one-hot编码使其向量化

            train_labels = np_utils.to_categorical(train_labels)
            valid_labels = np_utils.to_categorical(valid_labels)
            test_labels = np_utils.to_categorical(test_labels)
            print(len(train_labels[1,]))


            # 像素数据浮点化以便归一化
            train_images = train_images.astype('float32')
            valid_images = valid_images.astype('float32')
            test_images = test_images.astype('float32')

            # 将其归一化,图像的各像素值归一化到0~1区间
            # 目的是提升网络收敛速度，减少训练时间，同时适应值域在(0,1)之间的激活函数，
            # 此外，确保特征值权重一致，避免大值对误差值有较大影响
            train_images /= 255
            valid_images /= 255
            test_images /= 255

            self.train_images = train_images
            self.valid_images = valid_images
            self.test_images = test_images
            self.train_labels = train_labels
            self.valid_labels = valid_labels
            self.test_labels = test_labels
            self.nb_classes = len(train_labels[0])

# CNN网络模型类
class Model:
    def __init__(self):
        self.model = None
        # 建立模型

    def build_model(self, dataset,nb_classes):

        # 构建一个空的网络模型，它是一个线性堆叠模型，各神经网络层会被顺序添加，专业名称为序贯模型或线性堆叠模型
        self.model = Sequential()

        self.model.add(Convolution2D(32, 3, 3, border_mode='same',  # 'same'保留边界，'valid'丢掉边界部分
                                     input_shape=dataset.input_shape))  # 'tf'维度顺序,Conv1
        self.model.add(Activation('relu'))  # ƒ(x) = max(0, x) ，收敛快 ，训练效果佳

        self.model.add(Convolution2D(64, 3, 3, border_mode='same'))
        self.model.add(Activation('relu'))

        self.model.add(MaxPooling2D(pool_size=(2, 2),strides = 2))  #  池化层

        self.model.add(Convolution2D(64, 3, 3, border_mode='same'))
        self.model.add(Activation('relu'))

        self.model.add(Convolution2D(128, 3, 3, border_mode='same'))
        self.model.add(Activation('relu'))

        self.model.add(MaxPooling2D(pool_size=(2, 2), strides=2))  # 池化层
        self.model.add(Dropout(0.3))  # Dropout层,0.25

        self.model.add(Convolution2D(96, 3, 3, border_mode='same'))
        self.model.add(Activation('relu'))

        self.model.add(Convolution2D(192, 3, 3, border_mode='same'))
        self.model.add(Activation('relu'))

        self.model.add(MaxPooling2D(pool_size=(2, 2), strides=2))  # 池化层
        self.model.add(Dropout(0.3))  # Dropout层,0.25

        self.model.add(Convolution2D(128, 3, 3, border_mode='same'))
        self.model.add(Activation('relu'))

        self.model.add(Convolution2D(256, 3, 3, border_mode='same'))
        self.model.add(Activation('relu'))

        self.model.add(MaxPooling2D(pool_size=(2, 2), strides=2))  # 池化层
        self.model.add(Dropout(0.3))  # Dropout层,0.25

        self.model.add(Convolution2D(160, 3, 3, border_mode='same'))
        self.model.add(Activation('relu'))

        self.model.add(Convolution2D(320, 3, 3, border_mode='same'))
        self.model.add(Activation('relu'))

        self.model.add(AveragePooling2D(pool_size=(2, 2), strides=2))  # 池化层
        self.model.add(Dropout(0.3))  # Dropout层,0.25

        self.model.add(Flatten())  # Flatten层 , 二维转一维
        self.model.add(Dense(512))  # Dense层,又被称作全连接层,保留了512个特征输出到下一层
        self.model.add(Activation('relu'))  # 激活函数层
        self.model.add(Dropout(0.5))  # Dropout层,0.25
        self.model.add(Dense(nb_classes))  # Dense层，最终分类
        self.model.add(Activation('softmax'))  # 分类层，输出最终结果
        # 输出模型概况
        self.model.summary()

        # 训练模型
    def train(self, dataset, batch_size=60, nb_epoch=200, data_augmentation=True):

        sgd = SGD(lr=0.01, decay=5e-5,# best = 0.01,0.00005
                  momentum=0.9, nesterov=True)  # 采用SGD+momentum的优化器进行训练，首先生成一个优化器对象
        self.model.compile(loss='categorical_crossentropy',
                           optimizer=sgd,
                           metrics=['accuracy'])  # 完成实际的模型配置工作

        # 不使用数据提升，所谓的提升就是从我们提供的训练数据中利用旋转、翻转、加噪声等方法创造新的
        # 训练数据，有意识的提升训练数据规模，增加模型训练量
        if not data_augmentation:
            train_log = self.model.fit(dataset.train_images,
                           dataset.train_labels,
                           batch_size=batch_size,
                           nb_epoch=nb_epoch,
                           validation_data=(dataset.valid_images, dataset.valid_labels),
                           shuffle=True
                          )
        # 使用实时数据提升
        else:
            # 定义数据生成器用于数据提升，其返回一个生成器对象datagen，datagen每被调用一
            # 次其生成一组数据（顺序生成），节省内存，其实就是python的数据生成器
            datagen = ImageDataGenerator(
                featurewise_center=False,  # 是否使输入数据去中心化（均值为0），
                samplewise_center=False,  # 是否使输入数据的每个样本均值为0
                featurewise_std_normalization=False,  # 是否数据标准化（输入数据除以数据集的标准差）
                samplewise_std_normalization=False,  # 是否将每个样本数据除以自身的标准差
                zca_whitening=False,  # 是否对输入数据施以ZCA白化
                rotation_range=20,  # 数据提升时图片随机转动的角度(范围为0～180)
                width_shift_range=0.2,  # 数据提升时图片水平偏移的幅度（单位为图片宽度的占比，0~1之间的浮点数）
                height_shift_range=0.2,  # 同上，只不过这里是垂直
                horizontal_flip=True,  # 是否进行随机水平翻转
                vertical_flip=False)  # 是否进行随机垂直翻转

            # 计算整个训练样本集的数量以用于特征值归一化、ZCA白化等处理
            datagen.fit(dataset.train_images)


            # 利用生成器开始训练模型
            train_log = self.model.fit_generator(datagen.flow(dataset.train_images, dataset.train_labels,
                                                  batch_size=batch_size),
                                     samples_per_epoch=dataset.train_images.shape[0],
                                     nb_epoch=nb_epoch,
                                     validation_data=(dataset.valid_images, dataset.valid_labels)
                                     )

        # 损失函数和准确率画图
        plt.style.use("ggplot")
        plt.figure()
        plt.plot(np.arange(0, nb_epoch), train_log.history["loss"], label="train_loss")
        plt.plot(np.arange(0, nb_epoch), train_log.history["val_loss"], label="val_loss")
        plt.plot(np.arange(0, nb_epoch), train_log.history["acc"], label="train_acc")
        plt.plot(np.arange(0, nb_epoch), train_log.history["val_acc"], label="val_acc")
        plt.title("Training Loss and Accuracy on sar classifier")
        plt.xlabel("Epoch #")
        plt.ylabel("Loss/Accuracy")
        plt.legend(loc="upper right")
        plt.savefig("Loss_Accuracy_alexnet_{:d}e_a.jpg".format(nb_epoch))


    #保存模型
    def save_model(self, file_path=MODEL_PATH):
        self.model.save(file_path)

    #加载模型
    def load_model(self, file_path=MODEL_PATH):
        self.model = load_model(file_path)

    #模型评估
    def evaluate(self, dataset):
        score = self.model.evaluate(dataset.test_images, dataset.test_labels, verbose=1)
        print("%s: %.2f%%" % (self.model.metrics_names[1], score[1] * 100))




if __name__ == '__main__':
    #select_WebFace
    dataset = Dataset('G:\\code\\study\\source_code\\LFW\\select_WebFace')
    dataset.load()

    model = Model()
    #print(dataset.nb_classes)
    model.build_model(dataset,dataset.nb_classes)

    # 测试训练函数的代码
    model.train(dataset)
    model.save_model()

    model.load_model()
    model.evaluate(dataset)