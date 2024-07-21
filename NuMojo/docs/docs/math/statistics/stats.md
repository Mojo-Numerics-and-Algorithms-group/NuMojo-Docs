



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

- array
- axis

## sumall


```rust
sumall(array: NDArray[dtype]) -> SIMD[$0, 1]
```  
Summary  
  
Sum of all items in the array.  
  
Args:  

- array

## prod


```rust
prod(array: NDArray[dtype], axis: Int = 0) -> NDArray[$0]
```  
Summary  
  
Product of array elements over a given axis.  
  
Args:  

- array
- axis

## prodall


```rust
prodall(array: NDArray[dtype]) -> SIMD[$0, 1]
```  
Summary  
  
Product of all items in the array.  
  
Args:  

- array

## mean


```rust
mean(array: NDArray[dtype], axis: Int = 0) -> NDArray[$0]
```  
Summary  
  
Mean of array elements over a given axis. Args:     array: NDArray.     axis: The axis along which the mean is performed. Returns:     An NDArray.  
  
Args:  

- array
- axis

## meanall


```rust
meanall(array: NDArray[dtype]) -> SIMD[float64, 1]
```  
Summary  
  
Mean of all items in the array.  
  
Args:  

- array

## max


```rust
max[dtype: DType](array: NDArray[dtype], axis: Int = 0) -> NDArray[$0]
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- array
- axis

## min


```rust
min[dtype: DType](array: NDArray[dtype], axis: Int = 0) -> NDArray[$0]
```  
Summary  
  
  
  
Parameters:  

- dtype
  
Args:  

- array
- axis
