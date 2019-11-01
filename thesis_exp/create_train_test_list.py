import csv

csv_file_path = 'ThesisExp/train_test_accuracy_hl01.csv'
list_file_path = 'plot_values.csv'

train_accuracy_list = []
valid_accuracy_list = []
no_hdunits_list = []

with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    line_count = 0
    for row in csv_reader:

        no_hd_units = int(row[0])
        lr_rate = float(row[1])
        train_accuracy = float(row[2])
        valid_accuracy = float(row[3])
        if lr_rate == 0.00001:
            no_hdunits_list.append(no_hd_units)
            train_accuracy_list.append(train_accuracy)
            valid_accuracy_list.append(valid_accuracy)


with open('plot_values.csv', mode='w') as plot_values:
    plot_values_writer = csv.writer(plot_values, delimiter=',')
    plot_values_writer.writerow(no_hdunits_list)
    plot_values_writer.writerow(train_accuracy_list)
    plot_values_writer.writerow(valid_accuracy_list)