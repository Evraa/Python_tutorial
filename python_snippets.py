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
	#OR
	# train_acc = np.mean(y_val == y_val_pred)
	return accuracy

def foldNdArray(X_train, num_folds):
	'''
		Divide X_train into 'num_folds' arrays
	'''
	X_train_folds = np.array_split(X_train, num_folds)
	return X_train_folds

def maskFromTo (start=0, end, X_train):
	'''
		return the values from start to end only
	'''
	mask = list(range(start, end))
	#ie: mask = [5,6,7,8,9,10] 
    X_val = X_train[mask]
	return X_val 

def horizontalStack (X_train):
	'''
		Input: [[1 , 2, 3]
				[4, 5, 6]]

		output [[1, 2, 3, 1
				[4, 5, 6, 1]]
	'''
	return np.hstack([X_train, np.ones((X_train.shape[0], 1))])

def randomNdArray (rows, columns=1):
	return np.random.randn(rows, columns)

def sameShape(X_train):
	return np.zeros_like(X_train)

