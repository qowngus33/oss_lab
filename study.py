with open('data/class_score_en.csv', 'r') as fi, \
        open('class_score_mean_en.csv', 'w') as fo:
    for line in fi.readlines():
        try:
            values = [int(text) for text in line.split(',')]
            mean = sum(values) / len(values)
            for val in values:
                fo.write(f'{val}, ')
            fo.write(f'{mean}\n')
        except ValueError as ex: # Try 'FileNotFoundError' and 'Exception' (base class)
            print(f'A line is ignored. (message: {ex})')
