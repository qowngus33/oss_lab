from sklearn import metrics
import matplotlib.pyplot as plt

y_true = [False] * 90 + [True] * 10
y_pred = [False] * 99 + [True] * 1

print(metrics.accuracy_score(y_true, y_pred))
print(metrics.balanced_accuracy_score(y_true, y_pred))
print(metrics.precision_score(y_true, y_pred))
print(metrics.recall_score(y_true, y_pred))
print(metrics.f1_score(y_true, y_pred))
print(metrics.precision_recall_fscore_support(y_true, y_pred))
print(metrics.classification_report(y_true, y_pred))

conf_mat = metrics.confusion_matrix(y_true, y_pred)
conf_dis = metrics.ConfusionMatrixDisplay(conf_mat,display_labels=["-","+"])
conf_dis.plot()
plt.show()
