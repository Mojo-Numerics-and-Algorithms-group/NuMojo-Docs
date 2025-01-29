



# stats

##  Module Summary
  
Statistics functions for NDArray
## sum


```rust
sum(array: NDArray[dtype], axis: Int = 0) -> NDArray[$0]
```  
Summary  
  
Sum of array elements over a given axis.  
  
Args:  

- array: NDArray.
- axis: The axis along which the sum is performed. Default: 0

## sumall


```rust
sumall(array: NDArray[dtype]) -> SIMD[$0, 1]
```  
Summary  
  
Sum of all items in the array.  
  
Args:  

- array: NDArray.

## prod


```rust
prod(array: NDArray[dtype], axis: Int = 0) -> NDArray[$0]
```  
Summary  
  
Product of array elements over a given axis.  
  
Args:  

- array: NDArray.
- axis: The axis along which the product is performed. Default: 0

## prodall


```rust
prodall(array: NDArray[dtype]) -> SIMD[$0, 1]
```  
Summary  
  
Product of all items in the array.  
  
Args:  

- array: NDArray.

## mean


```rust
mean(array: NDArray[dtype], axis: Int = 0) -> NDArray[$0]
```  
Summary  
  
Mean of array elements over a given axis. Args:     array: NDArray.     axis: The axis along which the mean is performed. Returns:     An NDArray.  
  
Args:  

- array
- axis Default: 0

## meanall


```rust
meanall(array: NDArray[dtype]) -> SIMD[float64, 1]
```  
Summary  
  
Mean of all items in the array.  
  
Args:  

- array: NDArray.

## max


```rust
max[dtype: DType](array: NDArray[dtype], axis: Int = 0) -> NDArray[$0]
```  
Summary  
  
Maximums of array elements over a given axis.  
  
Parameters:  

- dtype
  
Args:  

- array: NDArray.
- axis: The axis along which the sum is performed. Default: 0

## min


```rust
min[dtype: DType](array: NDArray[dtype], axis: Int = 0) -> NDArray[$0]
```  
Summary  
  
Minumums of array elements over a given axis.  
  
Parameters:  

- dtype
  
Args:  

- array: NDArray.
- axis: The axis along which the sum is performed. Default: 0
