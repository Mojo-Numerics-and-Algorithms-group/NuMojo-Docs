



# sorting

##  Module Summary
  

## bubble_sort


```Mojo
bubble_sort[dtype: DType](ndarray: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Bubble sort the NDArray. Average complexity: O(n^2) comparisons, O(n^2) swaps. Worst-case complexity: O(n^2) comparisons, O(n^2) swaps. Worst-case space complexity: O(n).  
  
Parameters:  

- dtype: The input element type.
  
Args:  

- ndarray: An NDArray.


Example:
    ```py
    var arr = numojo.core.random.rand[numojo.i16](100)
    var sorted_arr = numojo.core.sort.bubble_sort(arr)
    print(sorted_arr)
    ```

## sort


```Mojo
sort[dtype: DType](owned A: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Sort NDArray using quick sort method. It is not guaranteed to be unstable.  
  
Parameters:  

- dtype: The input element type.
  
Args:  

- A: NDArray.


When no axis is given, the array is flattened before sorting.


```Mojo
sort[dtype: DType](owned A: NDArray[dtype], owned axis: Int) -> NDArray[dtype]
```  
Summary  
  
Sort NDArray along the given axis using quick sort method. It is not guaranteed to be unstable.  
  
Parameters:  

- dtype: The input element type.
  
Args:  

- A: NDArray to sort.
- axis: The axis along which the array is sorted.


When no axis is given, the array is flattened before sorting.

## binary_sort


```Mojo
binary_sort[dtype: DType = float64](array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Binary sorting of NDArray.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A NDArray.


Example:
    ```py
    var arr = numojo.core.random.rand[numojo.i16](100)
    var sorted_arr = numojo.core.sort.binary_sort(arr)
    print(sorted_arr)
    ```

## argsort_inplace


```Mojo
argsort_inplace[dtype: DType](mut ndarray: NDArray[dtype], mut idx_array: NDArray[index], left: Int, right: Int)
```  
Summary  
  
Conduct Argsort (in-place) based on the NDArray using quick sort.  
  
Parameters:  

- dtype: The input element type.
  
Args:  

- ndarray: An NDArray.
- idx_array: An NDArray of the indices.
- left: Left index of the partition.
- right: Right index of the partition.

## argsort


```Mojo
argsort[dtype: DType](ndarray: NDArray[dtype]) -> NDArray[index]
```  
Summary  
  
Argsort of the NDArray using quick sort algorithm.  
  
Parameters:  

- dtype: The input element type.
  
Args:  

- ndarray: An NDArray.


Example:
    ```py
    var arr = numojo.core.random.rand[numojo.i16](100)
    var sorted_arr = numojo.core.sort.argsort(arr)
    print(sorted_arr)
    ```
