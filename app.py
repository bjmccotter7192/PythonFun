import struct
import numpy as np
import matplotlib.pyplot as plt
import sys
import gzip

def read_image(file_name, idx_image):
#file_name: If used for the MNIST dataset, should be either 
#train-images-idx3-ubyte or t10k-images-idx3-ubyte
#index of the image you want to read.

    img_file = open(file_name,'r+b')
    print(img_file)
##########################################
# Get basic information about the images #
# (This is described in the webpage of 	 #
# the database)							 #
##########################################
    img_file.seek(0)
    magic_number = img_file.read(4)
    magic_number = struct.unpack('>i',magic_number)
    print('Magic Number: '+str(magic_number[0]))
    data_type = img_file.read(4)
    data_type = struct.unpack('>i',data_type)
    print('Number of Images: '+str(data_type[0]))
    dim = img_file.read(8)
    dimr = struct.unpack('>i',dim[0:4])
    dimr = dimr[0]
    print('Number of Rows: '+str(dimr))
    dimc = struct.unpack('>i',dim[4:])
    dimc = dimc[0]
    print('Number of Columns:'+str(dimc))
    image = np.ndarray(shape=(dimr,dimc))
    img_file.seek(16+dimc*dimr*idx_image)
    for row in range(dimr):
        for col in range(dimc):
            tmp_d = img_file.read(1)
            tmp_d = struct.unpack('>B',tmp_d)
            image[row,col] = tmp_d[0]
    img_file.close()
    return image

image = read_image("train-images.idx3-ubyte",1)

print(image.tolist())

img_plot = plt.imshow(image,'Greys')
plt.savefig('testFig.png')
plt.show()