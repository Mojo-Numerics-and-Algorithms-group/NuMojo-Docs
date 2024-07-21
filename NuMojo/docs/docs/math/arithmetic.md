



# arithmetic

##  Module Summary
  
Implements array arithmetic
## Aliases
  
`ln`: 
## add


```rust
add[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Perform addition on two arrays.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2


```rust
add[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Perform addition on between an array and a scalar.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array
- scalar


```rust
add[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Perform addition on between an array and a scalar.  
  
Parameters:  

- dtype
- backend
  
Args:  

- scalar
- array


```rust
add[dtype: DType, backend: Backend = Vectorized](owned *values: Variant[NDArray[dtype], SIMD[dtype, 1]]) -> NDArray[$0]
```  
Summary  
  
Perform addition on a list of arrays and a scalars.  
  
Parameters:  

- dtype
- backend
  
Args:  

- \*values: A list of arrays or Scalars to be added.

## sub


```rust
sub[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Perform subtraction on two arrays.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2


```rust
sub[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Perform subtraction on between an array and a scalar.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array
- scalar


```rust
sub[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Perform subtraction on between an array and a scalar.  
  
Parameters:  

- dtype
- backend
  
Args:  

- scalar
- array

## diff


```rust
diff[in_dtype: DType, out_dtype: DType = $0](array: NDArray[in_dtype], n: Int) -> NDArray[$1]
```  
Summary  
  
Compute the n-th order difference of the input array.  
  
Parameters:  

- in_dtype
- out_dtype
  
Args:  

- array
- n

## copysign


```rust
copysign[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Copy the sign of the first NDArray and apply it to the second NDArray.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2

## mod


```rust
mod[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise modulo of array1 and array2.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2


```rust
mod[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Perform subtraction on between an array and a scalar.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array
- scalar


```rust
mod[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Perform subtraction on between an array and a scalar.  
  
Parameters:  

- dtype
- backend
  
Args:  

- scalar
- array

## mul


```rust
mul[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise product of array1 and array2.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2


```rust
mul[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Perform multiplication on between an array and a scalar.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array
- scalar


```rust
mul[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Perform multiplication on between an array and a scalar.  
  
Parameters:  

- dtype
- backend
  
Args:  

- scalar
- array


```rust
mul[dtype: DType, backend: Backend = Vectorized](owned *values: Variant[NDArray[dtype], SIMD[dtype, 1]]) -> NDArray[$0]
```  
Summary  
  
Perform multiplication on a list of arrays an arrays and a scalars.  
  
Parameters:  

- dtype
- backend
  
Args:  

- \*values: A list of arrays or Scalars to be added.

## div


```rust
div[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise quotent of array1 and array2.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2


```rust
div[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Perform true division on between an array and a scalar.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array
- scalar


```rust
div[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Perform true division on between an array and a scalar.  
  
Parameters:  

- dtype
- backend
  
Args:  

- scalar
- array

## floor_div


```rust
floor_div[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise quotent of array1 and array2.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2


```rust
floor_div[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype], scalar: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Perform true division on between an array and a scalar.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array
- scalar


```rust
floor_div[dtype: DType, backend: Backend = Vectorized](scalar: SIMD[dtype, 1], array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Perform true division on between an array and a scalar.  
  
Parameters:  

- dtype
- backend
  
Args:  

- scalar
- array

## fma


```rust
fma[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype], array3: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Apply a SIMD level fuse multipy add function of three variables and one return to a NDArray.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2
- array3


```rust
fma[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype], simd: SIMD[dtype, 1]) -> NDArray[$0]
```  
Summary  
  
Apply a SIMD level fuse multipy add function of three variables and one return to a NDArray.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2
- simd

## remainder


```rust
remainder[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise remainders of NDArray.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2

## cbrt


```rust
cbrt[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise cuberoot of NDArray.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## rsqrt


```rust
rsqrt[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise reciprocal squareroot of NDArray.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## sqrt


```rust
sqrt[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise squareroot of NDArray.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## exp2


```rust
exp2[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Calculate elementwise two to the power of NDArray[i].  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## exp


```rust
exp[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Calculate elementwise euler's constant(e) to the power of NDArray[i].  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## expm1


```rust
expm1[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Calculate elementwise euler's constant(e) to the power of NDArray[i] minus1.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## scalb


```rust
scalb[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Calculate the scalb of array1 and array2.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2

## log


```rust
log[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise natural logarithm of NDArray.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## log2


```rust
log2[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise logarithm base two of NDArray.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## log10


```rust
log10[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise logarithm base ten of NDArray.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## log1p


```rust
log1p[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise natural logarithm of 1 plus NDArray.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## tabs


```rust
tabs[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise absolute value of NDArray.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## tfloor


```rust
tfloor[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise round down to nearest whole number of NDArray.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## tceil


```rust
tceil[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise round up to nearest whole number of NDArray.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## ttrunc


```rust
ttrunc[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise remove decimal value from float whole number of NDArray.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## tround


```rust
tround[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise round NDArray to whole number.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## roundeven


```rust
roundeven[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Performs elementwise banker's rounding on the elements of a NDArray.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array

## nextafter


```rust
nextafter[dtype: DType, backend: Backend = Vectorized](array1: NDArray[dtype], array2: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Computes the nextafter of the inputs.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array1
- array2

## invert


```rust
invert[dtype: DType, backend: Backend = Vectorized](array: NDArray[dtype]) -> NDArray[$0]
```  
Summary  
  
Elementwise invert of an array.  
  
Parameters:  

- dtype
- backend
  
Args:  

- array
