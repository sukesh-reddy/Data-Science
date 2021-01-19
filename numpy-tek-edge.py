##############
# Numpy
# Numerical Python
# it provides high performance multi-dimensional arrays 
# key features of numpy are :
#   - ndarrays, Broadcasting, Vectorization, Input/Output

# 1 - row-wise
# 0 - column wise
##########################
# one-dimensional arrays
#########################3#

array1 = np.array([1,2,3,4])  # Rank1-arrays
array1 = np.array([1,2,3,4],dtype = np.int64)  # Rank1-arrays
array1.shape
array1.size

###########################
# Two-dimnesinal arrays
###########################

array2 = np.array([[1,2,3,4],[5,6,7,8,9]])
array2.size


########################
# BroadCasting Methods
########################
zeros = np.zeros((2,2))

ones = np.ones((2,2))

one and zeros = np.eye(3,3)

random = np.random.random((2,5))

# indexing / slicing - np.array()[rows, columns]

# Addition (+ / np.add(x,y)) 
# multiplication (* / np.multiply(x,y))
# Boolean Indexing (a[a>2])

# sorting (array.sort())
# intersection(), setdiff(), in1d(), union1d(), 

# array in-addition
np.sum([[1,2,3],[4,5,6]], axis = 1)
