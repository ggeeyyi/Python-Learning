import numpy as np
images_0= np.load('images_0.npy')
images_1= np.load('images_1.npy')
images=np.concatenate([images_0, images_1], axis=0)
images_2=np.delete(images, [0,16,2], axis=0)
print(images_2)