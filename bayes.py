import csv

datain = []
dataout = []
datatest = []


def input_data():
    with open('data.csv') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)

                for row in reader:
                    datain.append(row)


def output_data():
    with open('test.csv') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)

                for row in reader:
                    datatest.append(row)


def statistic():
    yes = 0
    no = 0
    for e in datain:
        if e[-1] == 'true':
            yes += 1
        if e[-1] == 'false':
            no += 1
    return (yes, no)

input_data()
output_data()

p_yes = statistic()[0]
p_no = statistic()[1]




def calc_field(name: str):
    dict_name = {
            'A' : 1,
            'B' : 2,
            'C' : 3
            }
    p_name1_yes = 0
    p_name0_yes = 0
    p_name1_no = 0
    p_name0_no = 0
    for e in datain:
        if int(e[dict_name[name]]) == 1 and e[-1] == 'true':
            p_name1_yes += 1
        if int(e[dict_name[name]]) == 0 and e[-1] == 'true':
            p_name0_yes += 1
        if int(e[dict_name[name]]) == 1 and e[-1] == 'false':
            p_name1_no += 1
        if int(e[dict_name[name]]) == 0 and e[-1] == 'false':
            p_name0_no += 1

    return [(p_name1_yes/p_yes, p_name1_no/p_no), (p_name0_yes/p_yes, p_name0_no/p_no)]


def classifier():
    dict_name = {
            'A' : 1,
            'B' : 2,
            'C' : 3
            }
    result = []
    for e in datatest:
        p_name_yes = 1
        p_name_no = 1
        for name in ['A', 'B', 'C']:
            if int(e[dict_name[name]]) == 1:
                p_name_yes *= calc_field(name)[0][0]
                p_name_no *= calc_field(name)[0][1]
            if int(e[dict_name[name]]) == 0:
                p_name_yes *= calc_field(name)[1][0]
                p_name_no *= calc_field(name)[1][1]

        result.append((p_name_yes, p_name_no))
    return result

for i, e in enumerate(classifier()):
    datatest[i].pop(0)
    if e[0] > e[1]:
        print(f'the class label for a test sample {datatest[i]}: +')

    if e[0] < e[1]:
        print(f'the class label for a test sample {datatest[i]}: -')
