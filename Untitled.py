Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 12:01:12) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.


>>> import numpy
>>> numpy.__version__
'1.14.2'
>>> import numpy as np
>>> np.<TAB>
SyntaxError: invalid syntax
>>> np?
SyntaxError: invalid syntax
>>> import numpy as np
>>> np.random.seed(0)
>>> x1 = np.random.randint(10, size=6)	#one dimensional array
>>> x2 = np.random.randint(10, size=(3, 4))	# Two Dimensional Array
>>> x3 = np.random.randint(10, size=(3, 4, 5))  #Three-Dimensional Array
>>> print("x3 ndim: ", x3.ndim)
('x3 ndim: ', 3)
>>> print("x3 shape:", x3.shape)
('x3 shape:', (3, 4, 5))
>>> print("x3 size:", x3.size)
('x3 size:', 60)
>>> print(x3)
[[[8 1 5 9 8]
  [9 4 3 0 3]
  [5 0 2 3 8]
  [1 3 3 3 7]]

 [[0 1 9 9 0]
  [4 7 3 2 7]
  [2 0 0 4 5]
  [5 6 8 4 1]]

 [[4 9 8 1 1]
  [7 9 9 3 6]
  [7 2 0 3 5]
  [9 4 4 6 4]]]
>>> print("dtype:", x3.dtype)
('dtype:', dtype('int64'))
>>> print("itemsize:", x3.itemsize, "bytes")
('itemsize:', 8, 'bytes')
>>> print("nbytes:", x3.nbytes, "bytes")
('nbytes:', 480, 'bytes')
>>> x1
array([5, 0, 3, 3, 7, 9])
>>> x3
array([[[8, 1, 5, 9, 8],
        [9, 4, 3, 0, 3],
        [5, 0, 2, 3, 8],
        [1, 3, 3, 3, 7]],

       [[0, 1, 9, 9, 0],
        [4, 7, 3, 2, 7],
        [2, 0, 0, 4, 5],
        [5, 6, 8, 4, 1]],

       [[4, 9, 8, 1, 1],
        [7, 9, 9, 3, 6],
        [7, 2, 0, 3, 5],
        [9, 4, 4, 6, 4]]])
>>> x1
array([5, 0, 3, 3, 7, 9])
>>> x1[0]
5
>>> x1[4]
7
>>> x1[-1]
9
>>> x1[-2]
7
>>> x2
array([[3, 5, 2, 4],
       [7, 6, 8, 8],
       [1, 6, 7, 7]])
>>> x2[0, 0]
3
>>> x2[2, 1]
6
>>> x2[1, -1]
8
>>> x2[0, 0] = 12
>>> x2
array([[12,  5,  2,  4],
       [ 7,  6,  8,  8],
       [ 1,  6,  7,  7]])
>>> x1[0] = 3.1435
>>> x1
array([3, 0, 3, 3, 7, 9])
>>> x = np.arrange(10)

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    x = np.arrange(10)
AttributeError: 'module' object has no attribute 'arrange'
>>> x = np.arange(10)
>>> x
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> x[:5]
array([0, 1, 2, 3, 4])
>>> x[5:]
array([5, 6, 7, 8, 9])
>>> x[4:7]
array([4, 5, 6])
>>> x[::2]
array([0, 2, 4, 6, 8])
>>> x[1::3]
array([1, 4, 7])
>>> x[5::-2]
array([5, 3, 1])
>>> x2
array([[12,  5,  2,  4],
       [ 7,  6,  8,  8],
       [ 1,  6,  7,  7]])
>>> x2[:2, :3]
array([[12,  5,  2],
       [ 7,  6,  8]])
>>> x2[:3, 2:]
array([[2, 4],
       [8, 8],
       [7, 7]])
>>> x2[:3, ::2]
array([[12,  2],
       [ 7,  8],
       [ 1,  7]])
>>> x2[::-1, ::-1]
array([[ 7,  7,  6,  1],
       [ 8,  8,  6,  7],
       [ 4,  2,  5, 12]])
>>> print(x2[:, 0])
[12  7  1]
>>> print(x2[0, :])
[12  5  2  4]
>>> print(x2[-1, :])
[1 6 7 7]
>>> print(x2[0])
[12  5  2  4]
>>> # Subarray as no-copy views
>>> print(x2)
[[12  5  2  4]
 [ 7  6  8  8]
 [ 1  6  7  7]]
>>> x2_sub = x2[:2, :2]
>>> print(x2_sub)
[[12  5]
 [ 7  6]]
>>> x2_sub[0, 0] = 99
>>> print(x2_sub)
[[99  5]
 [ 7  6]]
>>> print(x2)
[[99  5  2  4]
 [ 7  6  8  8]
 [ 1  6  7  7]]
>>> #	Create copies of arrays
>>> x2_sub_copy = x2[:2, :2].copy()
>>> print(x2_sub_copy)
[[99  5]
 [ 7  6]]
>>> x2_sub_copy[0, 0] = 42
>>> print(x2_sub_copy)
[[42  5]
 [ 7  6]]
>>> print(x2)
[[99  5  2  4]
 [ 7  6  8  8]
 [ 1  6  7  7]]
>>> # Reshaping of Array
>>> grid = np.arange(1, 10).reshape((3, 3))
>>> print(grid)
[[1 2 3]
 [4 5 6]
 [7 8 9]]
>>> x = np.array([1, 2, 3])
>>> # row vector via reshape
>>> x.reshape((1, 3))
array([[1, 2, 3]])
>>> # row vector via new axis
>>> x[np.newaxis, :]
array([[1, 2, 3]])
>>> x.reshape((3, 1))
array([[1],
       [2],
       [3]])
>>> x[:, np.newaxis]
array([[1],
       [2],
       [3]])
>>> #concatenation
>>> x = np.array([1, 2, 3])
>>> y = np.array([3, 2, 1])
>>> np.concatenate([x, y])
array([1, 2, 3, 3, 2, 1])
>>> # concatenate along first axis
>>> np.concatenate([grid, grid], axis=1)
array([[1, 2, 3, 1, 2, 3],
       [4, 5, 6, 4, 5, 6],
       [7, 8, 9, 7, 8, 9]])
>>> z = [99, 99, 99]
>>> print(np.concatenate([x, y, z]))
[ 1  2  3  3  2  1 99 99 99]
>>> grid = np.array([[1, 2, 3],])
>>> grid = np.array([[1, 2, 3],
		 [4, 5, 6]])
>>> np.concatenate([grid, grid])
array([[1, 2, 3],
       [4, 5, 6],
       [1, 2, 3],
       [4, 5, 6]])
>>> x = np.array([1, 2, 3])
>>> grid = np.array([9, 8, 7],
		[6, 5, 4])

Traceback (most recent call last):
  File "<pyshell#88>", line 2, in <module>
    [6, 5, 4])
TypeError: data type not understood
>>> grid = np.array([[9, 8, 7],
		 [6, 5, 4]])
>>> np.vstack([x, grid])
array([[1, 2, 3],
       [9, 8, 7],
       [6, 5, 4]])
>>> np.hstack([grid,x])

Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    np.hstack([grid,x])
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/numpy/core/shape_base.py", line 288, in hstack
    return _nx.concatenate(arrs, 1)
ValueError: all the input arrays must have same number of dimensions
>>> y = np.array([[99],
	      [99]])
>>> np.hstack([grid, y])
array([[ 9,  8,  7, 99],
       [ 6,  5,  4, 99]])
>>> x = [1, 2, 3, 4, 5, 6, 7, 8]
>>> x1, x2, x3 = np.split(x, [3, 5])
>>> print(x1, x2, x3)
(array([1, 2, 3]), array([4, 5]), array([6, 7, 8]))
>>> grid = np.arange(16).reshape((4, 4))
>>> grid
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])
>>> upper, lower = np.vsplit(grid, [2])
>>> print(upper)
[[0 1 2 3]
 [4 5 6 7]]
>>> print(lower)
[[ 8  9 10 11]
 [12 13 14 15]]
>>> 
