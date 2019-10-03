import gzip
import json
import numpy as np
import matplotlib.pyplot as plt

trainImages = gzip.open('train-images-idx3-ubyte.gz', 'r')
trainLabels = gzip.open('train-labels-idx1-ubyte.gz', 'r')

image_size = 28
num_images = 5

trainImages.read(16)
buf = trainImages.read(image_size * image_size * num_images)
data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
data = data.reshape(num_images, image_size, image_size, 1)

image = np.asarray(data[4]).squeeze()
plt.imshow(image)
plt.show()