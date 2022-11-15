import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

def mean_var(data):
    n = len(data)
    if n > 0:
        mean = sum(data) / n
        sum2 = sum([datum**2 for datum in data])
        var = sum2 / n - mean**2
        return mean, var
    return None, None

if __name__ == "__main__":
    try:
        with open('../data/class_score_kr.csv', 'r') as fi, \
                open('class_score_mean.csv', 'w') as fo:
            for line in fi.readlines():
                try:
                    values = [int(text) for text in line.split(',')]
                    mean, var = mean_var(values)
                    for val in values:
                        fo.write(f'{val}, ')
                    fo.write(f'{mean}, {var}\n')
                except ValueError as ex:  # Try 'data/class_score_en.csv' without this try/except
                    print(f'A line is ignored.(message: {ex})')
    except Exception as ex:
        print(f'Cannot run the program. (message: {ex})')



