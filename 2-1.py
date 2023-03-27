import numpy as np
images_0= np.load('images_0.npy')
images_1= np.load('images_1.npy')
images=np.concatenate([images_0, images_1], axis=0)
print('元素数据类型：', images.dtype)
print('形状：', images.shape)
print(np.min(images))
print(np.max(images))
