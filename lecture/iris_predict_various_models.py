import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics,linear_model,naive_bayes,neural_network,neighbors,tree,ensemble
from matplotlib.colors import ListedColormap

iris = datasets.load_iris()
iris.data = iris.data[:,0:2]
iris.feature_names = iris.feature_names[0:2]
iris.color = np.array([(1,0,0),(0,1,0),(0,0,1)])

models = [
    {'name': 'linear_model.SGD',            'obj': linear_model.SGDClassifier()},
    {'name': 'naive_bayes.Gaussian',        'obj': naive_bayes.GaussianNB()},
    {'name': 'neural_network.MLP',          'obj': neural_network.MLPClassifier()},
    {'name': 'neighbors.KNN',               'obj': neighbors.KNeighborsClassifier()},
    {'name': 'svm.LinearSVC',               'obj': svm.LinearSVC()},
    {'name': 'svm.SVC(linear)',             'obj': svm.SVC(kernel='linear')},
    {'name': 'svm.SVC(poly,2)',             'obj': svm.SVC(kernel='poly', degree=2)},
    {'name': 'svm.SVC(poly,3)',             'obj': svm.SVC(kernel='poly')},
    {'name': 'svm.SVC(poly,4)',             'obj': svm.SVC(kernel='poly', degree=4)},
    {'name': 'svm.SVC(rbf)',                'obj': svm.SVC(kernel='rbf')},
    {'name': 'svm.SVC(rbf,$\gamma$=1)',     'obj': svm.SVC(kernel='rbf', gamma=1)},
    {'name': 'svm.SVC(rbf,$\gamma$=4)',     'obj': svm.SVC(kernel='rbf', gamma=4)},
    {'name': 'svm.SVC(rbf,$\gamma$=16)',    'obj': svm.SVC(kernel='rbf', gamma=16)},
    {'name': 'svm.SVC(rbf,$\gamma$=64)',    'obj': svm.SVC(kernel='rbf', gamma=64)},
    {'name': 'svm.SVC(sigmoid)',            'obj': svm.SVC(kernel='sigmoid')},
    {'name': 'tree.DecisionTree(2)',        'obj': tree.DecisionTreeClassifier(max_depth=2)},
    {'name': 'tree.DecisionTree(4)',        'obj': tree.DecisionTreeClassifier(max_depth=4)},
    {'name': 'tree.DecisionTree(N)',        'obj': tree.DecisionTreeClassifier()},
    {'name': 'tree.ExtraTree',              'obj': tree.ExtraTreeClassifier()},
    {'name': 'ensemble.RandomForest(10)',   'obj': ensemble.RandomForestClassifier(n_estimators=10)},
    {'name': 'ensemble.RandomForest(100)',  'obj': ensemble.RandomForestClassifier()},
    {'name': 'ensemble.ExtraTrees(10)',     'obj': ensemble.ExtraTreesClassifier()},
    {'name': 'ensemble.ExtraTrees(100)',    'obj': ensemble.ExtraTreesClassifier()},
    {'name': 'ensemble.AdaBoost(DTree)',    'obj': ensemble.AdaBoostClassifier(tree.DecisionTreeClassifier())},
]

x_min, x_max = iris.data[:,0].min() - 1, iris.data[:,0].max() + 1
y_min, y_max = iris.data[:,1].min() - 1, iris.data[:,1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min,x_max,0.01),np.arange(y_min,y_max,0.01))
xy = np.vstack((xx.flatten(),yy.flatten())).T

for model in models:
    model['obj'].fit(iris.data,iris.target)

    predict = model['obj'].predict(iris.data)
    model['acc'] = metrics.balanced_accuracy_score(iris.target, predict)

    zz = model['obj'].predict(xy)
    plt.contourf(xx, yy, zz.reshape(xx.shape), cmap=ListedColormap(iris.color), alpha=0.2)

    plt.title(model['name'] + f' ({model["acc"]:.3f})')
    plt.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.color[iris.target], edgecolors=iris.color[predict])
    plt.xlabel(iris.feature_names[0])
    plt.ylabel(iris.feature_names[1])
    plt.show()
