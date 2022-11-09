import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, tree, ensemble, metrics
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D

# Load a dataset partially
iris = datasets.load_iris()
iris.data = iris.data[:,0:2]
iris.feature_names = iris.feature_names[0:2]
iris.color = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)])

# Train a model
model = tree.DecisionTreeClassifier(max_depth=4) # Try deeper
model.fit(iris.data, iris.target)

# Visualize training results (decision boundaries)
x_min, x_max = iris.data[:, 0].min() - 1, iris.data[:, 0].max() + 1
y_min, y_max = iris.data[:, 1].min() - 1, iris.data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
xy = np.vstack((xx.flatten(), yy.flatten())).T
zz = model.predict(xy)
plt.contourf(xx, yy, zz.reshape(xx.shape), cmap=ListedColormap(iris.color), alpha=0.2)

# Test the model
predict = model.predict(iris.data)
accuracy = metrics.balanced_accuracy_score(iris.target, predict)

clabel = [Line2D([0],[0],marker='o',lw=0,label=iris.target_names[i], color=iris.color[i]) for i in range(len(iris.color))]

# Visualize testing results
plt.title(f'Decision tree ({accuracy:.3f})')
plt.scatter(iris.data[:,0], iris.data[:,1], c=iris.color[iris.target], edgecolors=iris.color[predict])
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.legend(handles=clabel,framealpha=0.5)
plt.show()

# Visualize training results (the trained tree)
tree.plot_tree(model, feature_names=iris.feature_names, class_names=iris.target_names, impurity=False)
plt.show()
