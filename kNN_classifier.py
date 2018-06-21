from numpy imprt *
import operator

#create a database for learning
def createDataSet():
  group = array([1.0,1.1],[1.0,1.0],[0,0],[0,0.1])
  labels = [ 'a','a','b','b' ]
  return group, labels
  
#kNN classifier

def classify0(inX, dataSet, labels, k):
  dataSetSize = dataSet.shape(0) #get the shape of data
  diffMat = tile(inX, (dataSetSize,1)) - dataSet #get diff of input x from data points in matrix format
  sqDiffMat = diffMat**2 #square of matrix
  sqDistances = sqDiffMat.sum(axis=1) #distances square
  distances = sqDistances**0.5 #distnce of input from points
  sortedDistIndices = distances.argsort() #sorting of indices
  for i in range(k): 
    voteIlabel = labels[sortedDistIndices[i]]  #
    classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
  sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse = true)
  return sortedClassCount [0][0]
