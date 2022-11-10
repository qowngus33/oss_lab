import numpy as np
from sklearn import (datasets, tree, model_selection, svm, ensemble)
from warnings import simplefilter

# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

if __name__ == '__main__':
    # Load a dataset
    wdbc = datasets.load_breast_cancer()

    # Train a model
    model = ensemble.RandomForestClassifier(random_state=24)

    param_grid = {
        'n_estimators': [10, 25, 50, 75, 100, 200, 500],
        'max_depth': [2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 20, 1000],
        'min_samples_leaf': [2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 32],
        'min_samples_split': [1, 2, 4, 8, 10, 12, 14, 16, 20, 24, 32],
    }

    cv_grid_search = model_selection.GridSearchCV(estimator=model, param_grid=param_grid, cv=5,verbose=2)
    cv_grid_search.fit(wdbc.data, wdbc.target)
    print("best model parameter and score: ")
    print(cv_grid_search.best_params_,cv_grid_search.best_score_)

    cv_results = model_selection.cross_validate(model, wdbc.data, wdbc.target, cv=5, return_train_score=True)

    # Evaluate the model
    acc_train = np.mean(cv_results['train_score'])
    acc_test = np.mean(cv_results['test_score'])
    print(f'* Accuracy @ training data: {acc_train:.3f}')
    print(f'* Accuracy @ test data: {acc_test:.3f}')
    print(f'* Your score: {max(10 + 100 * (acc_test - 0.9), 0):.0f}')
    print(model.max_samples)
