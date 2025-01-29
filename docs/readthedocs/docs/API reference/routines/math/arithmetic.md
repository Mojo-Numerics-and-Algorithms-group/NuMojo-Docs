



# arithmetic

##  Module Summary
  
Implements arithmetic operations functions
## add


```rust
add[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Perform addition on two arrays.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.


```rust
add[dtype: DType, backend: Backend = Vectorized, *, OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](array1: NDArray[dtype], array2: NDArray[OtherDType]) -> NDArray[ResultDType]
```  
Summary  
  
Perform addition on two arrays.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
- OtherDType: The element type of the second array.
- ResultDType: The element type of the result array. Defualt: `result[::DType,::DType]()`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.


```rust
add[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[dtype]
```  
Summary  
  
Perform addition on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.
- scalar: A NDArray.


```rust
add[dtype: DType, backend: Backend = Vectorized, *, OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](array: NDArray[dtype], scalar: SIMD[OtherDType, 1]) -> NDArray[ResultDType]
```  
Summary  
  
Perform addition on two arrays.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
- OtherDType: The element type of the second array.
- ResultDType: The element type of the result array. Defualt: `result[::DType,::DType]()`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array: A NDArray.
- scalar: A NDArray.


```rust
add[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Perform addition on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- scalar: A NDArray.
- array: A NDArray.


```rust
add[dtype: DType, backend: Backend = Vectorized, *, OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](scalar: SIMD[dtype, 1], array: NDArray[OtherDType]) -> NDArray[ResultDType]
```  
Summary  
  
Perform addition on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
- OtherDType: The element type of the second array.
- ResultDType: The element type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- scalar: A NDArray.
- array: A NDArray.


```rust
add[dtype: DType, backend: Backend = Vectorized](owned *values: Variant[NDArray[dtype], SIMD[dtype, 1]]) -> NDArray[dtype]
```  
Summary  
  
Perform addition on a list of arrays and a scalars.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- \*values: A list of arrays or Scalars to be added.

## sub


```rust
sub[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Perform subtraction on two arrays.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.


```rust
sub[dtype: DType, backend: Backend = Vectorized, *, OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](array1: NDArray[dtype], array2: NDArray[OtherDType]) -> NDArray[ResultDType]
```  
Summary  
  
Perform subtraction on two arrays.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
- OtherDType: The element type of the second array.
- ResultDType: The element type of the result array. Defualt: `result[::DType,::DType]()`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.


```rust
sub[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[dtype]
```  
Summary  
  
Perform subtraction on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.
- scalar: A NDArray.


```rust
sub[dtype: DType, backend: Backend = Vectorized, *, OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](array: NDArray[dtype], scalar: SIMD[OtherDType, 1]) -> NDArray[ResultDType]
```  
Summary  
  
Perform subtraction on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
- OtherDType: The element type of the second array.
- ResultDType: The element type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- array: A NDArray.
- scalar: A NDArray.


```rust
sub[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Perform subtraction on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- scalar: A NDArray.
- array: A NDArray.


```rust
sub[dtype: DType, backend: Backend = Vectorized, *, OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](scalar: SIMD[dtype, 1], array: NDArray[OtherDType]) -> NDArray[ResultDType]
```  
Summary  
  
Perform subtraction on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
- OtherDType: The element type of the second array.
- ResultDType: The element type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- scalar: A NDArray.
- array: A NDArray.

## diff


```rust
diff[dtype: DType = float64](array: NDArray[dtype], n: Int) -> NDArray[dtype]
```  
Summary  
  
Compute the n-th order difference of the input array.  
  
Parameters:  

- dtype: The element type. Defualt: `float64`
  
Args:  

- array: A array.
- n: The order of the difference.

## mod


```rust
mod[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Element-wise modulo of array1 and array2.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.


```rust
mod[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[dtype]
```  
Summary  
  
Perform subtraction on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.
- scalar: A NDArray.


```rust
mod[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Perform subtraction on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- scalar: A NDArray.
- array: A NDArray.

## mul


```rust
mul[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Element-wise product of array1 and array2.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.


```rust
mul[dtype: DType, backend: Backend = Vectorized, *, OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](array1: NDArray[dtype], array2: NDArray[OtherDType]) -> NDArray[ResultDType]
```  
Summary  
  
Perform multiplication on between two arrays.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
- OtherDType: The element type of the second array.
- ResultDType: The element type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- array1: A NDArray.
- array2: A NDArray.


```rust
mul[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[dtype]
```  
Summary  
  
Perform multiplication on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.
- scalar: A NDArray.


```rust
mul[dtype: DType, backend: Backend = Vectorized, *, OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](array: NDArray[dtype], scalar: SIMD[OtherDType, 1]) -> NDArray[ResultDType]
```  
Summary  
  
Perform multiplication on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
- OtherDType: The element type of the second array.
- ResultDType: The element type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- array: A NDArray.
- scalar: A NDArray.


```rust
mul[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Perform multiplication on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- scalar: A NDArray.
- array: A NDArray.


```rust
mul[dtype: DType, backend: Backend = Vectorized, *, OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](scalar: SIMD[dtype, 1], array: NDArray[OtherDType]) -> NDArray[ResultDType]
```  
Summary  
  
Perform multiplication on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
- OtherDType: The element type of the second array.
- ResultDType: The element type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- scalar: A NDArray.
- array: A NDArray.


```rust
mul[dtype: DType, backend: Backend = Vectorized](owned *values: Variant[NDArray[dtype], SIMD[dtype, 1]]) -> NDArray[dtype]
```  
Summary  
  
Perform multiplication on a list of arrays an arrays and a scalars.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- \*values: A list of arrays or Scalars to be added.

## div


```rust
div[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Element-wise quotent of array1 and array2.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.


```rust
div[dtype: DType, backend: Backend = Vectorized, *, OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](array1: NDArray[dtype], array2: NDArray[OtherDType]) -> NDArray[ResultDType]
```  
Summary  
  
Perform true division on between two arrays.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
- OtherDType: The element type of the second array.
- ResultDType: The element type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- array1: A NDArray.
- array2: A NDArray.


```rust
div[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[dtype]
```  
Summary  
  
Perform true division on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.
- scalar: A NDArray.


```rust
div[dtype: DType, backend: Backend = Vectorized, *, OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](array: NDArray[dtype], scalar: SIMD[OtherDType, 1]) -> NDArray[ResultDType]
```  
Summary  
  
Perform true division on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
- OtherDType: The element type of the second array.
- ResultDType: The element type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- array: A NDArray.
- scalar: A NDArray.


```rust
div[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Perform true division on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- scalar: A NDArray.
- array: A NDArray.


```rust
div[dtype: DType, backend: Backend = Vectorized, *, OtherDType: DType, ResultDType: DType = result[::DType,::DType]()](scalar: SIMD[dtype, 1], array: NDArray[OtherDType]) -> NDArray[ResultDType]
```  
Summary  
  
Perform true division on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defualts to `Vectorized`. Defualt: `Vectorized`
- OtherDType: The element type of the second array.
- ResultDType: The element type of the result array. Defualt: `result[::DType,::DType]()`
  
Args:  

- scalar: A NDArray.
- array: A NDArray.

## floor_div


```rust
floor_div[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Element-wise quotent of array1 and array2.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.


```rust
floor_div[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[dtype]
```  
Summary  
  
Perform true division on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- array: A NDArray.
- scalar: A NDArray.


```rust
floor_div[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Perform true division on between an array and a scalar.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Args:  

- scalar: A NDArray.
- array: A NDArray.

## fma


```rust
fma[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Apply a SIMD level fuse multipy add function of three variables and one return to a NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shape.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.
- array3: A NDArray.


```rust
fma[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype], simd: SIMD[dtype, 1]) -> NDArray[dtype]
```  
Summary  
  
Apply a SIMD level fuse multipy add function of three variables and one return to a NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shape  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.
- simd: A SIMD[dtype,1] value to be added.

## remainder


```rust
remainder[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[dtype]
```  
Summary  
  
Element-wise remainders of NDArray.  
  
Parameters:  

- dtype: The element type.
- backend: Sets utility function origin, defaults to `Vectorized`. Defualt: `Vectorized`
  
Constraints:

Both arrays must have the same shapes.  
  
Args:  

- array1: A NDArray.
- array2: A NDArray.
