#function to calculate Shannon entropy of a dataset
import operator

from math import log
def calcShannonEnt(dataSet):
  numEntries = len(dataSet)
  labelCounts = {}
  for featVec in dataSet
    currentLabel = featVec[-1]
    if currentLabel not in labelCounts.keys():
      labelCounts[currentLabel] = 0
      labelCounts[currentLabel] += 1
  shannonEnt = 0.0
  for key in labelCounts:
    prob = float(labelCounts[key])/numEntries
    shannonEnt -= prob*log(prob,2)
  return shannonEnt
  
#fuction to create a dummy dataset

def createDataSet():
  dataSet = [[1, 1, 'yes'],
 [1, 1, 'yes'],
 [1, 0, 'no'],
 [0, 1, 'no'],
 [0, 1, 'no']]
  labels = ['no surfacing','flippers']
  return dataSet, labels
  
#function to split dataset

def splitDataSet(dataSet, axis, value):
  retDataSet = []
  for featVec in dataSet:
     if featVec[axis] == value:
        reducedFeatVec = featVec[:axis]
        reducedFeatVec.extend(featVec[axis+1:])
        retDataSet.append(reducedFeatVec)
  return retDataSet

#choosing best feature to split on

def chooseBest(dataSet):
  numfeatures = len(dataSet[0]) - 1
  baseEntropy = calcShannonEnt(dataSet)
  bestInfogain = 0.0
  bestFeature = -1
  for i in range(numFeatures):
    featList = [example[i] for example in dataSet]
    uniqueVals = set(featList)
    newEntropy = 0.0
    for value in uniqueVals:
      subDataSet = splitDataSet(dataSet, i, value)
      prob = len(subDataSet)/float(len(dataSet))
      newEntropy += prob*clacShannonEnt(subDataSet) 
    infoGain = baseEntropy - newEntropy
    if (infoGain > bestInfoGain)
      bestInfogain = infoGain
      bestFeature = i
  return bestFeature
  
  def majorityCnt(classList):
    classCount = {}
    for vote in classList:
      if vote not in classCount.keys(): classCount[vote] = 0
      classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]
  
def createTree(dataSet, labels):
  classList = [example[-1] for example in dataSet]
  


        
  

  
