



# matrix

##  Module Summary
  
`numojo.Matrix` provides:
## Matrix

### Matrix Summary
  
  
`Matrix` is a special case of `NDArray` (2DArray) but has some targeted optimization since the number of dimensions is known at the compile time. It has simpler indexing and slicing methods, which is very useful when users only want to work with 2-dimensional arrays.  

### Parent Traits
  

- AnyType
- CollectionElement
- Copyable
- Movable
- Sized
- Stringable
- UnknownDestructibility
- Writable

### Aliases
  
`width`: Vector size of the data type.
### Fields
  
  
* shape `Tuple[Int, Int]`  
    - Shape of Matrix.  
* size `Int`  
    - Size of Matrix.  
* strides `Tuple[Int, Int]`  
    - Strides of matrix.  
* flags `Dict[String, Bool]`  
    - Information about the memory layout of the array.  

### Functions

#### __init__


```rust
__init__(out self, shape: Tuple[Int, Int])
```  
Summary  
  
Construct a matrix without initializing data.  
  
Args:  

- self
- shape: List of shape.


```rust
__init__(out self, data: Self)
```  
Summary  
  
Construct a matrix from matrix.  
  
Args:  

- self
- data


```rust
__init__(out self, data: NDArray[dtype])
```  
Summary  
  
Construct a matrix from array.  
  
Args:  

- self
- data

#### __copyinit__


```rust
__copyinit__(out self, other: Self)
```  
Summary  
  
Copy other into self.  
  
Args:  

- self
- other

#### __moveinit__


```rust
__moveinit__(out self, owned other: Self)
```  
Summary  
  
Move other into self.  
  
Args:  

- self
- other

#### __del__


```rust
__del__(owned self)
```  
Summary  
  
  
  
Args:  

- self

#### __getitem__


```rust
__getitem__(self, owned x: Int, owned y: Int) -> SIMD[dtype, 1]
```  
Summary  
  
Return the scalar at the index.  
  
Args:  

- self
- x: The row number.
- y: The column number.


```rust
__getitem__(self, owned x: Int) -> Self
```  
Summary  
  
Return the corresponding row at the index.  
  
Args:  

- self
- x: The row number.


```rust
__getitem__(self, x: Slice, y: Slice) -> Self
```  
Summary  
  
Get item from two slices.  
  
Args:  

- self
- x
- y


```rust
__getitem__(self, x: Slice, owned y: Int) -> Self
```  
Summary  
  
Get item from one slice and one int.  
  
Args:  

- self
- x
- y


```rust
__getitem__(self, owned x: Int, y: Slice) -> Self
```  
Summary  
  
Get item from one int and one slice.  
  
Args:  

- self
- x
- y


```rust
__getitem__(self, indices: List[Int]) -> Self
```  
Summary  
  
Get item by a list of integers.  
  
Args:  

- self
- indices

#### __setitem__


```rust
__setitem__(self, x: Int, y: Int, value: SIMD[dtype, 1])
```  
Summary  
  
Return the scalar at the index.  
  
Args:  

- self
- x: The row number.
- y: The column number.
- value: The value to be set.


```rust
__setitem__(self, owned x: Int, value: Self)
```  
Summary  
  
Set the corresponding row at the index with the given matrix.  
  
Args:  

- self
- x: The row number.
- value: Matrix (row vector).

#### __lt__


```rust
__lt__(self, other: Self) -> Matrix[bool]
```  
Summary  
  
  
  
Args:  

- self
- other


```rust
__lt__(self, other: SIMD[dtype, 1]) -> Matrix[bool]
```  
Summary  
  
Matrix less than scalar.  
  
Args:  

- self
- other

#### __le__


```rust
__le__(self, other: Self) -> Matrix[bool]
```  
Summary  
  
  
  
Args:  

- self
- other


```rust
__le__(self, other: SIMD[dtype, 1]) -> Matrix[bool]
```  
Summary  
  
Matrix less than and equal to scalar.  
  
Args:  

- self
- other

#### __eq__


```rust
__eq__(self, other: Self) -> Matrix[bool]
```  
Summary  
  
  
  
Args:  

- self
- other


```rust
__eq__(self, other: SIMD[dtype, 1]) -> Matrix[bool]
```  
Summary  
  
Matrix less than and equal to scalar.  
  
Args:  

- self
- other

#### __ne__


```rust
__ne__(self, other: Self) -> Matrix[bool]
```  
Summary  
  
  
  
Args:  

- self
- other


```rust
__ne__(self, other: SIMD[dtype, 1]) -> Matrix[bool]
```  
Summary  
  
Matrix less than and equal to scalar.  
  
Args:  

- self
- other

#### __gt__


```rust
__gt__(self, other: Self) -> Matrix[bool]
```  
Summary  
  
  
  
Args:  

- self
- other


```rust
__gt__(self, other: SIMD[dtype, 1]) -> Matrix[bool]
```  
Summary  
  
Matrix greater than scalar.  
  
Args:  

- self
- other

#### __ge__


```rust
__ge__(self, other: Self) -> Matrix[bool]
```  
Summary  
  
  
  
Args:  

- self
- other


```rust
__ge__(self, other: SIMD[dtype, 1]) -> Matrix[bool]
```  
Summary  
  
Matrix greater than and equal to scalar.  
  
Args:  

- self
- other

#### __add__


```rust
__add__(self, other: Self) -> Self
```  
Summary  
  
  
  
Args:  

- self
- other


```rust
__add__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Add matrix to scalar.  
  
Args:  

- self
- other

#### __sub__


```rust
__sub__(self, other: Self) -> Self
```  
Summary  
  
  
  
Args:  

- self
- other


```rust
__sub__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Subtract matrix by scalar.  
  
Args:  

- self
- other

#### __mul__


```rust
__mul__(self, other: Self) -> Self
```  
Summary  
  
  
  
Args:  

- self
- other


```rust
__mul__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Mutiply matrix by scalar.  
  
Args:  

- self
- other

#### __matmul__


```rust
__matmul__(self, other: Self) -> Self
```  
Summary  
  
  
  
Args:  

- self
- other

#### __truediv__


```rust
__truediv__(self, other: Self) -> Self
```  
Summary  
  
  
  
Args:  

- self
- other


```rust
__truediv__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Divide matrix by scalar.  
  
Args:  

- self
- other

#### __pow__


```rust
__pow__(self, rhs: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Power of items.  
  
Args:  

- self
- rhs

#### __radd__


```rust
__radd__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Right-add.  
  
Args:  

- self
- other

#### __rsub__


```rust
__rsub__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Right-sub.  
  
Args:  

- self
- other

#### __rmul__


```rust
__rmul__(self, other: SIMD[dtype, 1]) -> Self
```  
Summary  
  
Right-mul.  
  
Args:  

- self
- other

#### __iter__


```rust
__iter__(self) -> _MatrixIter[self, dtype]
```  
Summary  
  
Iterate over elements of the Matrix, returning copied value.  
  
Args:  

- self

#### __len__


```rust
__len__(self) -> Int
```  
Summary  
  
Returns length of 0-th dimension.  
  
Args:  

- self

#### __reversed__


```rust
__reversed__(self) -> _MatrixIter[self, dtype, False]
```  
Summary  
  
Iterate backwards over elements of the Matrix, returning copied value.  
  
Args:  

- self

#### __str__


```rust
__str__(self) -> String
```  
Summary  
  
  
  
Args:  

- self

#### write_to


```rust
write_to[W: Writer](self, mut writer: W)
```  
Summary  
  
  
  
Parameters:  

- W
  
Args:  

- self
- writer

#### all


```rust
all(self) -> SIMD[dtype, 1]
```  
Summary  
  
Test whether all array elements evaluate to True.  
  
Args:  

- self


```rust
all(self, axis: Int) -> Self
```  
Summary  
  
Test whether all array elements evaluate to True along axis.  
  
Args:  

- self
- axis

#### any


```rust
any(self) -> SIMD[dtype, 1]
```  
Summary  
  
Test whether any array elements evaluate to True.  
  
Args:  

- self


```rust
any(self, axis: Int) -> Self
```  
Summary  
  
Test whether any array elements evaluate to True along axis.  
  
Args:  

- self
- axis

#### argmax


```rust
argmax(self) -> SIMD[index, 1]
```  
Summary  
  
Index of the max. It is first flattened before sorting.  
  
Args:  

- self


```rust
argmax(self, axis: Int) -> Matrix[index]
```  
Summary  
  
Index of the max along the given axis.  
  
Args:  

- self
- axis

#### argmin


```rust
argmin(self) -> SIMD[index, 1]
```  
Summary  
  
Index of the min. It is first flattened before sorting.  
  
Args:  

- self


```rust
argmin(self, axis: Int) -> Matrix[index]
```  
Summary  
  
Index of the min along the given axis.  
  
Args:  

- self
- axis

#### argsort


```rust
argsort(self) -> Matrix[index]
```  
Summary  
  
Argsort the Matrix. It is first flattened before sorting.  
  
Args:  

- self


```rust
argsort(self, axis: Int) -> Matrix[index]
```  
Summary  
  
Argsort the Matrix along the given axis.  
  
Args:  

- self
- axis

#### astype


```rust
astype[asdtype: DType](self) -> Matrix[asdtype]
```  
Summary  
  
Copy of the matrix, cast to a specified type.  
  
Parameters:  

- asdtype
  
Args:  

- self

#### cumprod


```rust
cumprod(self) -> Self
```  
Summary  
  
Cumprod of flattened matrix.  
  
Args:  

- self


```rust
cumprod(self, axis: Int) -> Self
```  
Summary  
  
Cumprod of Matrix along the axis.  
  
Args:  

- self
- axis: 0 or 1.

#### cumsum


```rust
cumsum(self) -> Self
```  
Summary  
  
  
  
Args:  

- self


```rust
cumsum(self, axis: Int) -> Self
```  
Summary  
  
  
  
Args:  

- self
- axis

#### fill


```rust
fill(self, fill_value: SIMD[dtype, 1])
```  
Summary  
  
Fill the matrix with value.  
  
Args:  

- self
- fill_value

#### flatten


```rust
flatten(self) -> Self
```  
Summary  
  
Return a flattened copy of the matrix.  
  
Args:  

- self

#### inv


```rust
inv(self) -> Self
```  
Summary  
  
Inverse of matrix.  
  
Args:  

- self

#### max


```rust
max(self) -> SIMD[dtype, 1]
```  
Summary  
  
Find max item. It is first flattened before sorting.  
  
Args:  

- self


```rust
max(self, axis: Int) -> Self
```  
Summary  
  
Find max item along the given axis.  
  
Args:  

- self
- axis

#### mean


```rust
mean(self) -> SIMD[dtype, 1]
```  
Summary  
  
Calculate the arithmetic average of all items in the Matrix.  
  
Args:  

- self


```rust
mean(self, axis: Int) -> Self
```  
Summary  
  
Calculate the arithmetic average of a Matrix along the axis.  
  
Args:  

- self
- axis: 0 or 1.

#### min


```rust
min(self) -> SIMD[dtype, 1]
```  
Summary  
  
Find min item. It is first flattened before sorting.  
  
Args:  

- self


```rust
min(self, axis: Int) -> Self
```  
Summary  
  
Find min item along the given axis.  
  
Args:  

- self
- axis

#### prod


```rust
prod(self) -> SIMD[dtype, 1]
```  
Summary  
  
Product of all items in the Matrix.  
  
Args:  

- self


```rust
prod(self, axis: Int) -> Self
```  
Summary  
  
Product of items in a Matrix along the axis.  
  
Args:  

- self
- axis: 0 or 1.

#### reshape


```rust
reshape(self, shape: Tuple[Int, Int]) -> Self
```  
Summary  
  
Change shape and size of matrix and return a new matrix.  
  
Args:  

- self
- shape

#### resize


```rust
resize(mut self, shape: Tuple[Int, Int])
```  
Summary  
  
Change shape and size of matrix in-place.  
  
Args:  

- self
- shape

#### round


```rust
round(self, decimals: Int) -> Self
```  
Summary  
  
  
  
Args:  

- self
- decimals

#### std


```rust
std(self, ddof: Int = 0) -> SIMD[dtype, 1]
```  
Summary  
  
Compute the standard deviation.  
  
Args:  

- self
- ddof: Delta degree of freedom. Default: 0


```rust
std(self, axis: Int, ddof: Int = 0) -> Self
```  
Summary  
  
Compute the standard deviation along axis.  
  
Args:  

- self
- axis: 0 or 1.
- ddof: Delta degree of freedom. Default: 0

#### sum


```rust
sum(self) -> SIMD[dtype, 1]
```  
Summary  
  
Sum up all items in the Matrix.  
  
Args:  

- self


```rust
sum(self, axis: Int) -> Self
```  
Summary  
  
Sum up the items in a Matrix along the axis.  
  
Args:  

- self
- axis: 0 or 1.

#### trace


```rust
trace(self) -> SIMD[dtype, 1]
```  
Summary  
  
Transpose of matrix.  
  
Args:  

- self

#### transpose


```rust
transpose(self) -> Self
```  
Summary  
  
Transpose of matrix.  
  
Args:  

- self

#### T


```rust
T(self) -> Self
```  
Summary  
  
  
  
Args:  

- self

#### variance


```rust
variance(self, ddof: Int = 0) -> SIMD[dtype, 1]
```  
Summary  
  
Compute the variance.  
  
Args:  

- self
- ddof: Delta degree of freedom. Default: 0


```rust
variance(self, axis: Int, ddof: Int = 0) -> Self
```  
Summary  
  
Compute the variance along axis.  
  
Args:  

- self
- axis: 0 or 1.
- ddof: Delta degree of freedom. Default: 0

#### to_ndarray


```rust
to_ndarray(self) -> NDArray[dtype]
```  
Summary  
  
Create `NDArray` from `Matrix`.  
  
Args:  

- self

#### to_numpy


```rust
to_numpy(self) -> PythonObject
```  
Summary  
  
See `numojo.core.utility.to_numpy`.  
  
Args:  

- self

#### full


```rust
full[dtype: DType = float64](shape: Tuple[Int, Int], fill_value: SIMD[dtype, 1] = SIMD(0)) -> Matrix[dtype]
```  
Summary  
  
Return a matrix with given shape and filled value.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- shape
- fill_value Default: SIMD(0)

#### zeros


```rust
zeros[dtype: DType = float64](shape: Tuple[Int, Int]) -> Matrix[dtype]
```  
Summary  
  
Return a matrix with given shape and filled with zeros.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- shape

#### ones


```rust
ones[dtype: DType = float64](shape: Tuple[Int, Int]) -> Matrix[dtype]
```  
Summary  
  
Return a matrix with given shape and filled with ones.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- shape

#### identity


```rust
identity[dtype: DType = float64](len: Int) -> Matrix[dtype]
```  
Summary  
  
Return a matrix with given shape and filled value.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- len

#### rand


```rust
rand[dtype: DType = float64](shape: Tuple[Int, Int]) -> Matrix[dtype]
```  
Summary  
  
Return a matrix with random values uniformed distributed between 0 and 1.  
  
Parameters:  

- dtype: The data type of the NDArray elements. Defualt: `float64`
  
Args:  

- shape: The shape of the Matrix.

#### fromlist


```rust
fromlist[dtype: DType](object: List[SIMD[dtype, 1]], shape: Tuple[Int, Int] = Tuple(VariadicPack(<store_to_mem({0}), store_to_mem({0})>, True))) -> Matrix[dtype]
```  
Summary  
  
Create a matrix from a 1-dimensional list into given shape.  
  
Parameters:  

- dtype
  
Args:  

- object
- shape Default: Tuple(VariadicPack(<store_to_mem({0}), store_to_mem({0})>, True))

#### fromstring


```rust
fromstring[dtype: DType = float64](text: String, shape: Tuple[Int, Int] = Tuple(VariadicPack(<store_to_mem({0}), store_to_mem({0})>, True))) -> Matrix[dtype]
```  
Summary  
  
Matrix initialization from string representation of an matrix.  
  
Parameters:  

- dtype Defualt: `float64`
  
Args:  

- text: String representation of a matrix.
- shape: Shape of the matrix. Default: Tuple(VariadicPack(<store_to_mem({0}), store_to_mem({0})>, True))

## broadcast_to


```rust
broadcast_to[dtype: DType](A: Matrix[dtype], shape: Tuple[Int, Int]) -> Matrix[dtype]
```  
Summary  
  
Broadcase the vector to the given shape.  
  
Parameters:  

- dtype
  
Args:  

- A
- shape


```rust
broadcast_to[dtype: DType](A: SIMD[dtype, 1], shape: Tuple[Int, Int]) -> Matrix[dtype]
```  
Summary  
  
Broadcase the scalar to the given shape.  
  
Parameters:  

- dtype
  
Args:  

- A
- shape
