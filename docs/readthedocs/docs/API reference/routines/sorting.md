



# sorting

##  Module Summary
  
Sorting.
## sort


```rust
sort[dtype: DType](a: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Sort NDArray using quick sort method. It is not guaranteed to be unstable. When no axis is given, the output array is flattened to 1d.  
  
Parameters:  

- dtype: The input element type.
  
Args:  

- a: NDArray.


```rust
sort[dtype: DType](owned a: NDArray[dtype], axis: Int) -> NDArray[dtype]
```  
Summary  
  
Sort NDArray along the given axis using quick sort method. It is not guaranteed to be unstable. When no axis is given, the array is flattened before sorting.  
  
Parameters:  

- dtype: The input element type.
  
Args:  

- a: NDArray to sort.
- axis: The axis along which the array is sorted.


```rust
sort[dtype: DType](A: Matrix[dtype]) -> Matrix[dtype]
```  
Summary  
  
Sort the Matrix. It is first flattened before sorting.  
  
Parameters:  

- dtype
  
Args:  

- A


```rust
sort[dtype: DType](owned A: Matrix[dtype], axis: Int) -> Matrix[dtype]
```  
Summary  
  
Sort the Matrix along the given axis.  
  
Parameters:  

- dtype
  
Args:  

- A
- axis

## argsort


```rust
argsort[dtype: DType](a: NDArray[dtype]) -> NDArray[index]
```  
Summary  
  
Returns the indices that would sort an array. It is not guaranteed to be unstable. When no axis is given, the array is flattened before sorting.  
  
Parameters:  

- dtype: The input element type.
  
Args:  

- a: NDArray.


```rust
argsort[dtype: DType](a: NDArray[dtype], axis: Int) -> NDArray[index]
```  
Summary  
  
Returns the indices that would sort an array. It is not guaranteed to be unstable. When no axis is given, the array is flattened before sorting.  
  
Parameters:  

- dtype: The input element type.
  
Args:  

- a: NDArray to sort.
- axis: The axis along which the array is sorted.


```rust
argsort[dtype: DType](A: Matrix[dtype]) -> Matrix[index]
```  
Summary  
  
Argsort the Matrix. It is first flattened before sorting.  
  
Parameters:  

- dtype
  
Args:  

- A


```rust
argsort[dtype: DType](owned A: Matrix[dtype], axis: Int) -> Matrix[index]
```  
Summary  
  
Argsort the Matrix along the given axis.  
  
Parameters:  

- dtype
  
Args:  

- A
- axis

## binary_sort_1d


```rust
binary_sort_1d[dtype: DType](a: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- a

## binary_sort


```rust
binary_sort[dtype: DType = float64](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Binary sorting of NDArray.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A NDArray.

## bubble_sort


```rust
bubble_sort[dtype: DType](ndarray: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Bubble sort the NDArray. Average complexity: O(n^2) comparisons, O(n^2) swaps. Worst-case complexity: O(n^2) comparisons, O(n^2) swaps. Worst-case space complexity: O(n).  
  
Parameters:  

- dtype: The input element type.
  
Args:  

- ndarray: An NDArray.

## quick_sort_1d


```rust
quick_sort_1d[dtype: DType](a: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Sort array using quick sort method. Regardless of the shape of input, it is treated as a 1-d array. It is not guaranteed to be unstable.  
  
Parameters:  

- dtype: The input element type.
  
Args:  

- a: An 1-d array.

## argsort_quick_sort_1d


```rust
argsort_quick_sort_1d[dtype: DType](a: NDArray[dtype]) -> NDArray[index]
```  
Summary  
  
Returns the indices that would sort the buffer of an array. Regardless of the shape of input, it is treated as a 1-d array. It is not guaranteed to be unstable.  
  
Parameters:  

- dtype: The input element type.
  
Args:  

- a: NDArray.
