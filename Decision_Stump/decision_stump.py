import sys

def test_split(index, value, dataset):
	left, right = list(), list()
	for row in dataset:
		if row[index] < value:
			left.append(row)
		else:
			right.append(row)
	return left, right

def get_index(groups, classes):
	sums_rows_cols = float(sum([len(group) for group in groups]))
	gini = 0.0
	for group in groups:
		size = float(len(group))
		if size == 0:
			continue
		score = 0.0
		for class_val in classes:
			p = [row[-1] for row in group].count(class_val) / size
			score += p * p
		gini += (1.0 - score) * (size / sums_rows_cols)
	return gini

def gini(dataset):
	class_values = list(set(row[-1] for row in dataset))
	best_index = 0
	best_value = 0
	best_score = 1
	for index in range(len(dataset[0])-1):
		for row in dataset:
			groups = test_split(index, row[index], dataset)
			gini_score = get_index(groups, class_values)
			if gini_score < best_score:
				best_index = index
				best_value = row[index]
				best_score = gini_score
	return [best_index,best_value]

def toMatrixArray(textFile, labelsFile):
    linefromFile = textFile.readline()
    linefromLabels = labels_file.readline()
    matrixArray = []
    while (linefromFile != ''):
        a = linefromFile.split()
        b = linefromLabels.split()
        l2 = []
        for j in range(0, len(a), 1):
            l2.append((float(a[j])))
            if(j == len(a)-1):
                l2.append(b[0])
        matrixArray.append(l2)
        linefromLabels = labels_file.readline()
        linefromFile = textFile.readline()
    return matrixArray


datafile_name = sys.argv[1]
labelsfile_name = sys.argv[2]
labels_file = open(labelsfile_name, "r")
data_file = open(datafile_name, "r")
data_label_matrix = toMatrixArray(data_file,labels_file)

gini = gini(data_label_matrix)

print("Column Number:",gini[0],"Value:",gini[1])