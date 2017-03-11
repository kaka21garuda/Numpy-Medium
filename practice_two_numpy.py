import numpy as np

current_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
numpy_array = np.array(current_list)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

numpy_array.shape
# the shape of numpy_array would be:
# (3, 3)

numpy_array.reshape(9, 1)
# after reshaping happens, 9 rows and 1 column
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]
#  [7]
#  [8]
#  [9]]
