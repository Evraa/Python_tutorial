import numpy as np
   
def return_random_x (listOfItems, x):
	'''
		Returns random x elements of the listOfItems, with no duplicates
	'''
	return np.random.choice(listOfItems, x, replace=False)

def reshapeRemain(ndArray):
	'''
		Given (10K, 32,32,3) shape of ndArray
		returns (10K, 3072)
	'''
	return = np.reshape(ndArray, (ndArray.shape[0], -1))

def calcAccuracy(y_test, y_test_pred):
	'''
		Compute and print the fraction of correctly predicted examples
	'''
	#VICTORIZED code is always better...
	num_correct = np.sum(y_test_pred == y_test)
	accuracy = float(num_correct) / num_test
	return accuracy

def foldNdArray(X_train, num_folds):
	'''
		Divide X_train into 'num_folds' arrays
	'''
	X_train_folds = np.array_split(X_train, num_folds)
	return X_train_folds

