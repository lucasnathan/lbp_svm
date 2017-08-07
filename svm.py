import numpy as np
from skimage import io
import os
import glob
from skimage.feature import local_binary_pattern
import matplotlib.pyplot as plt
from skimage.color import label2rgb
from sklearn import svm
from sklearn import metrics
from sklearn.grid_search import GridSearchCV

images = []
label =  []
label_test = []
lbp_test = []
lbp = []
radius = 3
n_points = 81 * radius
eps = 1e-7

for filename in glob.glob(os.path.join('prac/*')):
	aux = io.imread(filename)
	images.append(aux)
	filename = os.path.basename(filename)
	label.append(filename.split("_")[0])
	lbp_item = local_binary_pattern(aux,n_points, radius, 'uniform')
	(hist, _) = np.histogram(lbp_item.ravel(),bins=np.arange(0, n_points + 3),range=(0, n_points + 2))
	# normalize the histogram
	hist = hist.astype("float")
	hist /= (hist.sum() + eps)
	lbp.append(hist)

for filename in glob.glob(os.path.join('test/*')):
	aux = io.imread(filename)
	images.append(aux)
	filename = os.path.basename(filename)
	label_test.append(filename.split("_")[0])
	lbp_item = local_binary_pattern(aux,n_points, radius, 'uniform')
	(hist, _) = np.histogram(lbp_item.ravel(),bins=np.arange(0, n_points + 3),range=(0, n_points + 2))
	# normalize the histogram
	hist = hist.astype("float")
	hist /= (hist.sum() + eps)
	lbp_test.append(hist)

# define range dos parametros
# C_range = 2. ** np.arange(-5,15,2)
# C_range = np.arange(10000,15000,1000)
# print C_range
# # gamma_range = 2. ** np.arange(3,-15,-2)
# k = [ 'linear']
# # k = ['linear','rbf','poly']
# param_grid = dict(C=C_range,kernel=k)
# #param_grid = dict(gamma=gamma_range, C=C_range,kernel=k)
# # # instancia o classificador, gerando probabilidades
# srv = svm.SVC(probability=True)
# #
# # # faz a busca
# grid = GridSearchCV(srv, param_grid, n_jobs=-1, verbose=True)
# grid.fit (lbp, label)
# #
# # # recupera o melhor modelo
# model = grid.best_estimator_
# #
# # # imprime os parametros desse modelo
# print grid.best_params_



# print images[0]
model = svm.SVC(C=15000,kernel='linear')
model.fit(lbp,label)
prediction = model.predict(lbp_test)

print metrics.classification_report(label_test,prediction)
print metrics.confusion_matrix(label_test,prediction)
