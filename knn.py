from numpy import *
import operator

def createDataset():
	''' Creating Dataset '''
	group = array([[1.0, 2.0], [1.0, 4.0], [4.0, 1.0], [4.0, 2.0]])
	labels = ['Action', 'Action', 'Romantic', 'Romantic']
	return group, labels

def calcDistance(inX, dataset, labels, k):
	""" Calculating Euclidean Distance """
	# shape is a tuple that gives dimensions of the array
    # shape[0] returns the number of rows, here will return 4
    # dataSet = [[1.0, 2.0], [1.0,4.0], [4.0, 1.0], [4.0, 2.0]]
    	datasetSize = dataset.shape[0]

    	diffMat = tile(inX, (datasetSize, 1)) - dataset

    	sqDiffMat = diffMat ** 2

    	sqDistances = sqDiffMat.sum(axis = 1)
   	distances = sqDistances ** 0.5
    	sortedDistIndices = distances.argsort()
    	return sortedDistIndices


def findMajorityClass(inX, dataset, labels, k, sortedDistIndices):
	""" Finding K Nearest Neighbors """
	classCount = {}
	# Maps labels to occurance counts    
	#iterate k times
	for i in range(k):
		voteILabel = labels[sortedDistIndices[i]]
		# increase +1 on selected labels
		classCount[voteILabel] = classCount.get(voteILabel, 0) + 1

	# sort in descending order
	return sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)

def classify0(inX, dataset, labels, k):
	
	sortedDistIndices = calcDistance(inX, dataset, labels, k)
	# take k items with lowest distances to inX and find majority class among k items
	sortedClassCount = findMajorityClass(inX, dataset, labels, k, sortedDistIndices)
	return sortedClassCount[0][0]

group, labels = createDataset()
result = classify0([2.0, 3.0], group, labels, 3)
print(result)
