from class_score_analysis import read_data
import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

if __name__ == "__main__":
    scores = np.array(read_data('../data/class_score_kr.csv'))

    midtm = [func(scores[:,0]) for func in [np.mean, np.var, np.std]]
    final = [func(scores[:,1]) for func in [np.mean, np.var, np.std]]

    cov_all = np.cov(scores.T, ddof=0)
    print(cov_all)

    cor_all = np.corrcoef(scores.T)
    print(cor_all)

