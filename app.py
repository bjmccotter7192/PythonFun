import struct
import numpy as np
import matplotlib.pyplot as plt
import sys

def read_image(file_name, idx_image):
    img_file = open(file_name,'r+b')

    img_file.seek(0)
    magic_number = img_file.read(4)
    magic_number = struct.unpack('>i',magic_number)

    # print('Magic Number: '+str(magic_number[0]))

    data_type = img_file.read(4)
    data_type = struct.unpack('>i',data_type)

    # print('Number of Images: '+str(data_type[0]))

    dim = img_file.read(8)
    dimr = struct.unpack('>i',dim[0:4])
    dimr = dimr[0]

    # print('Number of Rows: '+str(dimr))

    dimc = struct.unpack('>i',dim[4:])
    dimc = dimc[0]

    # print('Number of Columns:'+str(dimc))

    image = np.ndarray(shape=(dimr,dimc))
    img_file.seek(16+dimc*dimr*idx_image)

    for row in range(dimr):
        for col in range(dimc):
            tmp_d = img_file.read(1)
            tmp_d = struct.unpack('>B',tmp_d)
            image[row,col] = tmp_d[0]
    img_file.close()
    return image

def read_label(file_name, idx_image):
    img_file = open(file_name,'rb')

    img_file.seek(0)
    magic_number = img_file.read(4)
    magic_number = struct.unpack('>i',magic_number)[0]

    numImages = img_file.read(4)
    numImages = struct.unpack('>i',numImages)[0]

    labels = []
    for i in range(numImages):
        label = img_file.read(1)
        labels.append(struct.unpack('>B', label)[0])

    return labels[idx_image]

def flattenImage(image):
    imagesToList = image.tolist()
    flattenedImage = []

    for i in range(len(imagesToList)):
        flattenedImage = flattenedImage + imagesToList[i]

    print("Image for index: ")
    print(flattenedImage)

image = read_image("train-images.idx3-ubyte", 0)
label = read_label("train-labels.idx1-ubyte", 0)

print(image)
testing = np.reshape(image, 784)
print(testing)

img_plot = plt.imshow(image)
plt.show()