import gzip
import json
import numpy as np
import matplotlib.pyplot as plt

trainImages = gzip.open('train-images-idx3-ubyte.gz', 'r')
trainLabels = gzip.open('train-labels-idx1-ubyte.gz', 'r')

image_size = 28
num_images = 200

trainImages.read(16)
buf = trainImages.read(image_size * image_size * num_images)
data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
data = data.reshape(num_images, image_size, image_size, 1)
# test = data.reshape(748, 1)

print(np.asarray(data[1]))
print(test)

image = np.asarray(data[1]).squeeze()
plt.imshow(image)
# plt.savefig('testFig.png')
plt.show()