



# sort

##  Module Summary
  
Implements sort functions
## bubble_sort


```rust
bubble_sort[dtype: DType](ndarray: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Bubble sort the NDArray. Average complexity: O(n^2) comparisons, O(n^2) swaps. Worst-case complexity: O(n^2) comparisons, O(n^2) swaps. Worst-case space complexity: O(n).  
  
Parameters:  

- dtype
  
Args:  

- ndarray

## quick_sort_inplace


```rust
quick_sort_inplace[dtype: DType](inout ndarray: NDArray[dtype], left: Int, right: Int)
```  
Summary  
  
Quick sort (in-place) the NDArray.  
  
Parameters:  

- dtype
  
Args:  

- ndarray
- left
- right

## quick_sort


```rust
quick_sort[dtype: DType](ndarray: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Quick sort the NDArray. Adopt in-place partition. Average complexity: O(nlogn). Worst-case complexity: O(n^2). Worst-case space complexity: O(n). Unstable.  
  
Parameters:  

- dtype
  
Args:  

- ndarray

## binary_sort


```rust
binary_sort[in_dtype: DType, out_dtype: DType = float64](array: NDArray[in_dtype]) -> NDArray[$1]
```  
Summary  
  
Binary sorting of NDArray.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- array

## argsort_inplace


```rust
argsort_inplace[dtype: DType](inout ndarray: NDArray[dtype], inout idx_array: NDArray[index], left: Int, right: Int)
```  
Summary  
  
Conduct Argsort (in-place) based on the NDArray using quick sort.  
  
Parameters:  

- dtype
  
Args:  

- ndarray
- idx_array
- left
- right

## argsort


```rust
argsort[dtype: DType](ndarray: NDArray[dtype]) -> NDArray[index]
```  
Summary  
  
Argsort of the NDArray using quick sort algorithm.  
  
Parameters:  

- dtype
  
Args:  

- ndarray
