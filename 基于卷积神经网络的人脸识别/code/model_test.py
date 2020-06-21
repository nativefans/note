import cv2
from keras.models import load_model
import os
import re
path = 'G:\\code\\study\\source_code\\LFW\\yyp\\test_picture'
model = load_model('G:\\code\\study\\source_code\\LFW\\select_WebFace\\face_train_model_True_84.h5')
i = 0
j = 0
for pic_name in os.listdir(path):
    sort_num = re.sub('\D','',pic_name)
    pic_path = os.path.join(path,pic_name)
    image = cv2.imread(pic_path)
    #image = cv2.imread(pic_path, cv2.IMREAD_GRAYSCALE)
    #需要用reshape定义出例子的个数，图片的 通道数，图片的长与宽。具体的参考keras文档
    image = cv2.resize(image, (120, 120))
    img = (image.reshape(1, 120, 120, 3)).astype('int32')/255
    predict = model.predict_classes(img)
    print('图片类属:',sort_num)
    print ('识别为：',predict)
    print('-------------------------')
    j += 1
    if sort_num == re.sub('\D','',str(predict)):
        i += 1
print('准确率为:%d / %d' % (i,j))

