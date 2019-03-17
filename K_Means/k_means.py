from random import randint
import operator
import random
import sys


def to_list(filename):


    with open(filename, 'rt') as textfile:
        lines = textfile.readlines()
        matrix_array = [tuple(float(i) for i in line.split()) for line in lines]
        return matrix_array



def kmeans(data, k):


    ix = range(len(data))
    indexes = [i for i in random.sample(ix, k)]

    clusters = [[data[i]] for i in indexes]
    data = [element for n, element in enumerate(data) if n not in indexes]

    def calculate_centers(clust):

        def mean(it):
            n = len(it)
            return sum(it) / n

        centers = []
        for cluster in clust:
            if len(cluster) == 1:
                centers.append(cluster[0])
            else:
                centers.append(tuple(mean(i) for i in zip(*cluster)))
        return centers


    for point in data:
        centers = calculate_centers(clusters)
        minimum = 1000000
        ix = 0
        for x, center in enumerate(centers):
            diff = sum(abs(a - b) for a, b in zip(point, center))
            if diff < minimum:
                minimum = diff
                ix = x
        clusters[ix].append(point)

    arr = to_list(sys.argv[1])
    for i in range(len(arr)):
        for j in range(len(clusters)):
            if((clusters[j].count(arr[i]) == 1)):
                print(j, i)


k = int(sys.argv[2])
data = sys.argv[1]
kmeans(to_list(data), k)