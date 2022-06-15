#%%
# 먼저 pillow에 대해 알아보자
# 옛날 옛적에 파이썬에서의 이미지 처리를 위해 PIL(Python Image Library)이라는 라이브러리가 있었습니다.
# 하지만 이 라이브러리는 2011년 마지막 커밋을 이후로 개발이 중단되었습니다. 
# 대신 이 정신을 Pillow가 이어받아 현재까지도 지속적으로 이어져 내려오고 있습니다. 
# 오늘 학습의 주인공은 Pillow가 아니라 OpenCV입니다. 
# 그러나 간단한 이미지 작업에 Pillow는 Numpy와 결합하여 간편하게 사용할 수 있는 도구입니다. 
# 오늘 우리는 먼저 간단히 Pillow 사용법을 살펴보고 오늘 실습 데이터인 CIFAR-100 데이터를 전처리하는 작업을 진행해 보려고 합니다.

import numpy as np
from PIL import Image

data = np.zeros([32,32,3],dtype=np.uint8)
image = Image.fromarray(data, 'RGB')
image.show()

data[:, :] = [255, 0, 0]
image = Image.fromarray(data, 'RGB')
image
# %%
from PIL import Image
import os

# 연습용 파일 경로
image_path = os.getenv('HOME')+'/Working/Python3/opencv/data/pillow_practice.png'

# 이미지 열기
pimage = Image.open(image_path)
pimage

# width와 height 출력
print(pimage.width, pimage.height)
# JPG 파일 형식으로 저장해보기
im = pimage.convert('RGB')
im.save('data/pillow_parctice.jpg')
# %%
rim = im.resize((100,200))
rim
# %%
iim = im.crop((300, 100, 600, 400))
iim.save('data/eyes.png')
iim
# %%
import pickle
import os
from PIL import Image
dir_path = 'data/cifar-100-python'
train_filepath = os.path.join(dir_path, 'train')

with open(train_filepath, 'rb') as f:
    train = pickle.load(f,encoding='bytes')

print(type(train))
print(train)
# %%
print(train.keys())

image_data = train[b'data'][0].reshape([32, 32, 3], order='F')   # order를 주의하세요!!
image = Image.fromarray(image_data)    # Pillow를 사용하여 Numpy 배열을 Image객체로 만들어서
image    # 화면에 띄워 봅시다!!
# %%
image_data = image_data.swapaxes(0, 1) # 축을 바꿔줍니다!
image = Image.fromarray(image_data)
image
# %%


import os
import cv2 as cv
import numpy as np
from  matplotlib import pyplot as plt
%matplotlib inline

img_path = os.getenv('HOME')+'/Working/Python3/opencv/data/cv_practice.png'
img = cv.imread(img_path)

# Convert BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([100,100,100])
upper_blue = np.array([130,255,255])

# Threshold the HSV image to get only blue colors
mask = cv.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv.bitwise_and(img, img, mask=mask)

plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.show()
plt.imshow(cv.cvtColor(mask, cv.COLOR_BGR2RGB))
plt.show()
plt.imshow(cv.cvtColor(res, cv.COLOR_BGR2RGB))
plt.show()
# %%
