import numpy as np

image_path = "path_to_image.npy"

img = np.load(image_path)
from matplotlib import pyplot as plt
plt.imshow(img, cmap='gray')
plt.show()