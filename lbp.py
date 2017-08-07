import numpy as np
from skimage import io
import os
import glob
from skimage.feature import local_binary_pattern
import matplotlib.pyplot as plt
from skimage.color import label2rgb

images = []
label =  []
lbp = []
radius = 2
n_points = 6 * radius

for filename in glob.glob(os.path.join('prac/*')):
	aux = io.imread(filename)
	images.append(aux)
	lbp.append(local_binary_pattern(aux,n_points, radius, 'uniform'))
# print images[0]
