import numpy as np
from sklearn import (datasets, tree, model_selection, svm, ensemble)
from warnings import simplefilter

# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

if __name__ == '__main__':
    # Load a dataset
    wdbc = datasets.load_breast_cancer()

    # param_grid = {
    #     'n_estimators': [10, 20, 30, 40, 50, 75, 100],
    #     'max_depth': [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 100],
    #     'min_samples_leaf': [2, 3, 4, 5, 6, 7, 8, 10, 12],
    #     'min_samples_split': [2, 4, 6, 8, 10, 12],
    # }
    #
    # cv_grid_search = model_selection.GridSearchCV(estimator=model, param_grid=param_grid, cv=5,verbose=2)
    # cv_grid_search.fit(wdbc.data, wdbc.target)
    # print("best model parameter and score: ")
    # print(cv_grid_search.best_params_,cv_grid_search.best_score_)

    # Train a model
    model = ensemble.RandomForestClassifier(max_depth=8,min_samples_split=2,min_samples_leaf=2,n_estimators=40,random_state=33)

    cv_results = model_selection.cross_validate(model, wdbc.data, wdbc.target, cv=5, return_train_score=True)

    # Evaluate the model
    acc_train = np.mean(cv_results['train_score'])
    acc_test = np.mean(cv_results['test_score'])
    print(f'* Accuracy @ training data: {acc_train:.3f}')
    print(f'* Accuracy @ test data: {acc_test:.3f}')
    print(f'* Your score: {max(10 + 100 * (acc_test - 0.9), 0):.0f}')
