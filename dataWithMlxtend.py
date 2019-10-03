from mlxtend.data import loadlocal_mnist
import numpy as np
import gzip

trainImages = gzip.open('train-images-idx3-ubyte.gz', 'r')
trainLabels = gzip.open('train-labels-idx1-ubyte.gz', 'r')


X, y = loadlocal_mnist(trainImages, trainLabels)

print('Dimensions: %s x %s' % (X.shape[0], X.shape[1]))
print('\n1st row', X[0])

print('Digits:  0 1 2 3 4 5 6 7 8 9')
print('labels: %s' % np.unique(y))
print('Class distribution: %s' % np.bincount(y))

################ THIS WILL ONLY WORK IF YOU INSTALL MLXTEND FROM PIP #########################