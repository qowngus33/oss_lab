import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm
from matplotlib.lines import Line2D

# load dataset
iris = datasets.load_iris()

# train model
model = svm.SVC()
model.fit(iris.data, iris.target)

# test model
predict = model.predict(iris.data)
n_correct = sum(predict == iris.target)
accuracy = n_correct / len(iris.data)

# visualize
cmap = np.array([(1,0,0),(0,1,0),(0,0,1)]) # 3x3 array
clabel = [Line2D([0],[0],marker='o',lw=0,label=iris.target_names[i], color=cmap[i]) for i in range(len(cmap))]

for (x,y) in [(0,1),(2,3),(0,2),(0,3)]:
    plt.title(f'svm.SVC ({n_correct}/{len(iris.data)}={accuracy:.3f})')
    plt.scatter(iris.data[:,x], iris.data[:,y], c=cmap[iris.target],edgecolors=cmap[predict])
    plt.xlabel(iris.feature_names[x])
    plt.ylabel(iris.feature_names[y])
    plt.legend(handles=clabel,framealpha=0.5)
    plt.show()

