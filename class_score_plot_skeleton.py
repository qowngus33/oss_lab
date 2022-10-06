import matplotlib.pyplot as plt

def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if not line.startswith('#'): # If 'line' is not a header
                data.append([int(word) for word in line.split(',')])
    return data

if __name__ == '__main__':
    # Load score data
    class_kr = read_data('data/class_score_kr.csv')
    class_en = read_data('data/class_score_en.csv')

    # TODO) Prepare midterm, final, and total scores
    midtm_kr = [midtm for (midtm, _) in class_kr]
    final_kr = [final for (_, final) in class_kr]
    total_kr = [40/125*midtm + 60/100*final for (midtm, final) in class_kr]
    midtm_en = [0]
    final_en = [0]
    total_en = [0]

    # TODO) Plot midterm/final scores as points

    # TODO) Plot total scores as a histogram