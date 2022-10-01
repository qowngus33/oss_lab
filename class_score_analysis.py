def read_data(filename):
    data = []
    try:
        with open(filename, 'r') as fi:
            for line in fi.readlines():
                try:
                    if line[0] != '#':
                        values = [int(text) for text in line.split(',')]
                        temp = []
                        for val in values:
                            temp.append(int(val))
                        data.append(temp)
                except ValueError as ex:  # Try 'data/class_score_en.csv' without this try/except
                    print(f'A line is ignored.(message: {ex})')
    except Exception as ex:
        print(f'Cannot run the program. (message: {ex})')
    return data

def add_weighted_average(data, weight):
    for row in data:
        row.append(row[0]*weight[0] + row[1]*weight[1])

def mean_var(data):
    n = len(data)
    if n > 0:
        mean = sum(data) / n
        sum2 = sum([datum**2 for datum in data])
        var = sum2 / n - mean**2
        return mean, var
    return None, None

def analyze_data(data):
    n = len(data)
    mean = 0
    var = 0
    median = 0
    if n > 0:
        mean = sum(data) / n
        sum2 = sum([datum ** 2 for datum in data])
        var = sum2 / n - mean ** 2
    data.sort()

    if len(data) % 2 == 0:
        median = (data[len(data)/2-1]+data[len(data/2)])/2
    else:
        median = data[len(data)//2]

    return mean, var, median, min(data), max(data)

if __name__ == '__main__':
    data = read_data('data/class_score_en.csv')
    if data and len(data[0]) == 2: # Check 'data' is valid
        add_weighted_average(data, [40/125, 60/100])
        if len(data[0]) == 3:      # Check 'data' is valid
            print('### Individual Score')
            print()
            print('| Midterm | Final | Total |')
            print('| ------- | ----- | ----- |')
            for row in data:
                print(f'| {row[0]} | {row[1]} | {row[2]:.3f} |')
            print()

            print('### Examination Analysis')
            col_n = len(data[0])
            col_name = ['Midterm', 'Final', 'Total']
            colwise_data = [ [row[c] for row in data] for c in range(col_n) ]
            for c, score in enumerate(colwise_data):
                mean, var, median, min_, max_ = analyze_data(score)
                print(f'* {col_name[c]}')
                print(f'  * Mean: **{mean:.3f}**')
                print(f'  * Variance: {var:.3f}')
                print(f'  * Median: **{median:.3f}**')
                print(f'  * Min/Max: ({min_:.3f}, {max_:.3f})')