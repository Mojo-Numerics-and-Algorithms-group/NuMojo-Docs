



# sorting

##  Module Summary
  

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

## sort


```rust
sort[dtype: DType](owned A: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Sort NDArray using quick sort method. It is not guaranteed to be unstable.  
  
Parameters:  

- dtype: The input element type.
  
Args:  

- A: NDArray.


```rust
sort[dtype: DType](owned A: NDArray[dtype], owned axis: Int) -> NDArray[dtype]
```  
Summary  
  
Sort NDArray along the given axis using quick sort method. It is not guaranteed to be unstable.  
  
Parameters:  

- dtype: The input element type.
  
Args:  

- A: NDArray to sort.
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

## argsort


```rust
argsort[dtype: DType](owned A: NDArray[dtype]) -> NDArray[index]
```  
Summary  
  
Returns the indices that would sort an array. It is not guaranteed to be unstable.  
  
Parameters:  

- dtype: The input element type.
  
Args:  

- A: NDArray.


```rust
argsort[dtype: DType](owned A: NDArray[dtype], owned axis: Int) -> NDArray[index]
```  
Summary  
  
Returns the indices that would sort an array. It is not guaranteed to be unstable.  
  
Parameters:  

- dtype: The input element type.
  
Args:  

- A: NDArray to sort.
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
