import gzip
import json
from mnist import MNIST

mndata = MNIST('samples')
mndata.gz = True

images, labels = mndata.load_training()
# or
images, labels = mndata.load_testing()

index = random.randrange(0, len(images))
print(mndata.display(images[index]))